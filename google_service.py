import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/drive']

class GoogleService:
    def __init__(self):
        self.creds = None
        self.service = None
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
        self.service = build('drive', 'v3', credentials=self.creds)

    def get_files(self):
        try:
            results = self.service.files().list(
                pageSize=10, fields="nextPageToken, files(id, name)").execute()
            items = results.get('files', [])
            return items
        except HttpError as e:
            print(f'An error occurred: {e}')
            return None
 