import requests

# GET METHOD
def test_get_list_of_users():
    url = "https://reqres.in/api/users"
    response = requests.get(url)
    print("Get_response_code",response.status_code)
    print("Get_response", response)
    assert response.status_code == 200
        
# POST METHOD  
def test_create_new_user():
    url = "https://reqres.in/api/users"
    data = {
        "name": "Paulo Oliveira",
        "movies": ["I Love You Man", "Role Models"]
    }
    response = requests.post(url, data=data)
    print("Post_response_code", response.status_code)
    print("Post_response", response)
    assert response.status_code == 201
    
# UPDATE METHOD
def test_update_user():
    url = "https://reqres.in/api/users/2"
    data = {
        "name": "Paulo Updated"
    }
    response = requests.put(url, data=data)
    print("Update_response_code",response.status_code)
    print("Update_response", response)
    assert response.status_code == 200
    
# DELETE METHOD
def test_delete_user():
    url = "https://reqres.in/api/users/2"
    response = requests.delete(url)
    print("Delete_response_code",response.status_code)
    print("Delete_response", response)
    assert response.status_code == 204