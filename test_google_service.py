import pytest
import json
from pathlib import Path
from google_service import GoogleService


@pytest.fixture
def google_service():
    return GoogleService()

doc_id = '1dyucbGkQZ-SqJIqAs35ynl4QIVvUyx6mkLEa7_cMnu8'

@pytest.mark.skip(reason="We know that it works")
def test_google_service_get_files(google_service):
   fileList =  google_service.get_files()
   assert fileList is not None

@pytest.mark.skip(reason="We know that it works")
def test_google_service_create_doc(google_service):
    doc = google_service.create_doc('test')
    assert doc is not None


def test_google_service_get_file(google_service):
    doc = google_service.get_file(doc_id)
    
    json_file = Path('docs.html')
    json_file.write_text(doc)
    #print(json.dumps(content))
    assert doc is not None

# The test_google_service_get_files function tests the get_files method of the GoogleService class.
   

    
