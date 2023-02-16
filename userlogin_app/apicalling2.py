import requests
try:    
    response=requests.get("http://localhost:8000/getUser/Pratiksha")
    print(response.json())
except:
    
    print("No such record found")
    
    
