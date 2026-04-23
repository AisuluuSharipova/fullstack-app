import pytest
import json
from unittest.mock import patch, MagicMock
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200

def test_get_data_error(client):
    with patch('app.get_db', side_effect=Exception("No DB")):
        response = client.get('/api/data')
        assert response.status_code == 500

def test_post_data_error(client):
    with patch('app.get_db', side_effect=Exception("No DB")):
        response = client.post('/api/data',
            data=json.dumps({"title": "Test", "student_name": "Aibek", "student_id": "123"}),
            content_type='application/json')
        assert response.status_code == 500