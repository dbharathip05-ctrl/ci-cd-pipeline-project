# tests/test_app.py
from ci_cd_pipeline_app.app import app

def test_app():
    assert app is not None
    
    