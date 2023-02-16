import requests

try:    
    response=requests.get("http://localhost:8000/getUser2/Pratiksha")
    print(response.json())
except:
    
    print("No such record found")
    
    
