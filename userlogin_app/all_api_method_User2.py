import requests
print("Get User All Details Display without Serilizer")
try:    
    response=requests.get("http://localhost:8000/getUser/Pratiksha")
    print(response.json())
except:
     print("No such record found")
     
     

print("Get User All Details Display with Serilizer")
username=input("Enter Username=")
try:  
    response=requests.get("http://localhost:8000/getUser2/"+username)
    print(response.json())
except:   
    print("No such record found")

    

print("Add user using POST method")
try:  
    response=requests.post('http://localhost:8000/addUser2/',{'username':'Amol','password':'amol123','mobno':4567})
    print(response.text)
except:   
    print("No such record found")


print("Update user using PUT method")
try:  
    response=requests.put('http://localhost:8000/updateUser2/',{'username':'Amol','password':'amol123','mobno':9876})
    print(response.text)
except:   
    print("No such record found")


print("Delete user using DELETE method")
try:  
    response=requests.delete('http://localhost:8000/deleteUser2/Rudransh')
    print(response.text)
except:   
    print("No such record found")

    
    
