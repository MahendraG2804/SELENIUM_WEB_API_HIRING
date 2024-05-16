import requests

# POST METHOD 
Base_URL = "https://qa-hiringapi.topgrep.com"

def test_TC1_Login_Post_Request():
    url = Base_URL+"/api/auth"
    data = {
        "email": "hiring_robot_auto_test@getnada.com",
        "password": "hiring_robot_auto_test@getnada.coM"
    }
    response = requests.post(url, data=data)
    assert response.status_code == 200
    # print(response.content)
    jwt_token = response.json().get("token")  
    print("JWT Token:", jwt_token)  
    # print("RESPONSE", response.json())
    return jwt_token

# GET METHOD
def test_TC2_Login_Get_Request():
    jwt_token = test_TC1_Login_Post_Request()  
    # assert jwt_token is not None, "JWT token is None"  # Ensure token is fetched successfully    
    url = Base_URL+"/api/auth"
    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Content-Type": "application/json"
    }            
    response = requests.get(url, headers=headers)
    # print("GET Response:", response.json()) 
    assert response.status_code == 200
        
def test_TC3_Get_Job_Request():
    jwt_token = test_TC1_Login_Post_Request()      
    url =   Base_URL+"/api/jobs"
    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Content-Type": "application/json"
    }            
    response = requests.get(url, headers=headers)
    # print("GET Response:", response.json())  
    assert response.status_code == 200
    
def test_TC4_Post_Job_Request():
    jwt_token = test_TC1_Login_Post_Request()     
    url =  Base_URL+"/api/jobs"
    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Content-Type": "application/json"
     }     
    
    data = {
        "job_position": "QA",
        "descr": "QA IS RESPONSIBLE FOR QUALITY;'",
        "qualification": ["BE"],
        "responsibility": ["QUALITY CHECK"],
        "required_skills": [{"id": "HrMvvOpc6h5StDazT7-wN", "tag_name": "Automation"}],
        "questionnaire": None,
        "quiz": [],
        "live_assessment": [],
        "job_details": {
            "location": "BANGLORE",
            "type": "Part-Time",
            "experience": [0, 2]
        }
        }      
    response = requests.post(url, headers=headers, json=data)
    # print("GET Response:", response.json())  
    JOB_ID = response.json().get("id")  
    print("Job ID:", JOB_ID)
    assert response.status_code == 201
    return JOB_ID
   
# DELETE METHOD
def test_TC5_delete_user():
    jwt_token = test_TC1_Login_Post_Request() 
    id = test_TC4_Post_Job_Request()
    url =  Base_URL+f"/api/jobs/{id}"
    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Content-Type": "application/json"
     }     
    
    response = requests.delete(url, headers=headers)
    print("Delete_response_code",response.status_code)
    print("Delete_response", response)
    print("Res", response.content)
    assert response.status_code == 201
    
# # UPDATE METHOD
# def test_update_user():
#     url = "https://reqres.in/api/users/2"
#     data = {
#         "name": "Paulo Updated"
#     }
#     response = requests.put(url, data=data)
#     print("Update_response_code",response.status_code)
#     print("Update_response", response.content)
#     assert response.status_code == 200