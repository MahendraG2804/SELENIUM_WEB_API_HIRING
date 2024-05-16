import pytest
import requests

Base_URL = "https://qa-api.topgrep.com"
jwt_token = None
headers = {}

@pytest.fixture(scope="session")
def setup_jwt_token():
    global jwt_token
    if jwt_token is None:
        jwt_token = get_jwt_token()
        assert jwt_token is not None, "JWT token is None"
        headers["Authorization"] = f"Bearer {jwt_token}"
        headers["Content-Type"] = "application/json"

def get_jwt_token():
    url = Base_URL + "/api/auth"
    data = {
        "email": "mahendraqa@getnada.com",
        "password": "mahendraqa@getnada.coM"
    }
    response = requests.post(url, data=data)
    assert response.status_code == 200, f"Failed to get JWT token. Status code: {response.status_code}"
    jwt_token = response.json().get("token")
    print("JWT Token:", jwt_token)
    return jwt_token

def test_TC1_Login_Get_Request(setup_jwt_token):
    url = Base_URL + "/api/auth"
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Failed to authenticate. Status code: {response.status_code}"
    print("Respone:",response.text)
    assert "scholar" in response.text, "Expected content not found in response"

def test_TC2_Get_Jobs_Request(setup_jwt_token):
    url = Base_URL + "/api/hiring/job/posting/?page=1"
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Failed to get job request. Status code: {response.status_code}"
    print("Respone:",response.text)
#     assert "default_org_logo.png" in response.text, "Expected content not found in response"/api/hiring/job/posting/?page=1
#     assert type("job_details" in response.text == bool), "Job details should be a strdictionary"
        
# def test_TC3_Post_Job_Request(setup_jwt_token):
#     url = Base_URL + "/api/jobs"
#     data = {
#         "job_position": "QA",
#         "descr": "QA IS RESPONSIBLE FOR QUALITY;'",
#         "qualification": ["BE"],
#         "responsibility": ["QUALITY CHECK"],
#         "required_skills": [{"id": "HrMvvOpc6h5StDazT7-wN", "tag_name": "Automation"}],
#         "questionnaire": None,
#         "quiz": [],
#         "live_assessment": [],
#         "job_details": {
#             "location": "BANGLORE",
#             "type": "Part-Time",
#             "experience": [0, 2]
#         }
#     }
#     response = requests.post(url, headers=headers, json=data)
#     assert response.status_code == 201, f"Failed to post job request. Status code: {response.status_code}"
#     JOB_ID = response.json().get("id")
#     print("Job ID:", JOB_ID)
#     print("res", response.content)
#     return JOB_ID

# def test_TC4_delete_user(setup_jwt_token):
#     id = test_TC3_Post_Job_Request(setup_jwt_token)
#     url = Base_URL + f"/api/jobs/{id}"
#     response = requests.delete(url, headers=headers)
#     assert response.status_code == 200, f"Failed to delete user. Status code: {response.status_code}"
#     assert "Posting deleted successfully" in response.text, "Expected content not found in response"
#     print("res", response.text)