import requests

username=input("Enter Username=")
try:  
    response=requests.get("http://localhost:8000/getUser2/"+username)
    print(response.json())
except:
    
    print("No such record found")
    
