import requests

try:  
    response=requests.post('http://localhost:8000/addUser2/',{'username':'Amol','password':'amol123','mobno':4567})
    print(response.text)
except:   
    print("No such record found")
