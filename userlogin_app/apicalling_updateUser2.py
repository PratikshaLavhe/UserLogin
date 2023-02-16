import requests

try:  
    response=requests.put('http://localhost:8000/updateUser2/',{'username':'Amol','password':'amol123','mobno':9876})
    print(response.text)
except:   
    print("No such record found")
