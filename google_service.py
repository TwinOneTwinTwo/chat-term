import os
import io
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive']

class GoogleService:
    def __init__(self):
        self.creds = None
        self.drive_service = None
        self.docs_service = None
        self.token_file = 'token.json'
        self.credential_file = 'desk_top.json'
        self._authenticate()

    def _authenticate(self):
        if os.path.exists(self.token_file):
            self.creds = Credentials.from_authorized_user_file(self.token_file, SCOPES)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.credential_file, SCOPES)
                self.creds = flow.run_local_server(port=56067)
            with open(self.token_file, 'w') as token:
                token.write(self.creds.to_json())
        self.drive_service = build('drive', 'v3', credentials=self.creds)
        self.docs_service = build('docs', 'v1', credentials=self.creds)

    def get_file(self,file_id):
        try:
            req = self.drive_service.files().export_media( fileId=file_id, mimeType="text/html")
            file = io.BytesIO()
            downloader = MediaIoBaseDownload(file, req)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print(f"Download {int(status.progress() * 100)}.")

            return file.getvalue().decode('utf-8')
        
        except HttpError as e:
            print(f'An error occurred: {e}')
            return None
        
    def save_file(self, file_id,file_content, file_name) -> bool:
        try:
            if(file_id == None):
                # Create a new file
                file_metadata = {
                    'name': file_name,
                    'mimeType': 'application/vnd.google-apps.document'
                }
                file = self.drive_service.files().create(body=file_metadata, media_body=file_content).execute()

                
            else:
                file_metadata = {
                    'name': file_name,
                    'mimeType': 'application/vnd.google-apps.document'
                }
                file = self.drive_service.files().create(body=file_metadata, media_body=file_content).execute()

            return True
           
        except Exception as e:
            print(f'An error occurred: {e}')
            return False

    def delete_file(self, file_id):
        try:
            self.drive_service.files().delete(fileId=file_id).execute()
            return True
        except Exception as e:
            print(f'An error occurred: {e}')
            return False 
 
    