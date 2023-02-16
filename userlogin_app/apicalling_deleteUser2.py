import requests

try:  
    response=requests.delete('http://localhost:8000/deleteUser2/Rudransh')
    print(response.text)
except:   
    print("No such record found")
