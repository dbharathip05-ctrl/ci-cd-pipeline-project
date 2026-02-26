# tests/test_app.py
from ci_cd_pipeline_app.app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, CI/CD pipeline!" in response.data
    