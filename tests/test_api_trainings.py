import pytest
from utils import api_helpers

def test_api_trainings():
    headers = {
        'Authorization' : 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjY0LCJyb2xlIjoiY291bnRyeU93bmVyIiwicHJpbWFyeUNvbnRhY3ROYW1lIjoiSmFtZXMgTGllciIsImlhdCI6MTc1MDM1NTk5MSwiZXhwIjoxNzU4MTMxOTkxfQ.yiwGoTzV8Qec7QFkH9_EgSg8GIBfXCFs-u8mnqZIwqg'
    }
    response = api_helpers.get_all_trainings(headers)
    data = response.json()
    assert response.status_code == 200, 'should pass'
    assert 'data' in data, 'should pass'
    assert len(data) > 0,   'should pass'

