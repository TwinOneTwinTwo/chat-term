import pytest
from google_service import GoogleService


@pytest.fixture
def google_service():
    return GoogleService()

def test_google_service(google_service):
   fileList =  google_service.get_files()
   assert fileList is not None
   

    
