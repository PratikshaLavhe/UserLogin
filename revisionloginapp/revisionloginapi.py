import requests
import json

print("All Record Display using get method..")
response=requests.get("http://localhost:8000/getUser/Pratiksha/")
print(response.json())
print(json.dumps(response.json()))

print("Add Record using post method..")
response=requests.post("http://localhost:8000/addUser/",{"id":101,"Name":"Payal","City":"Baramati"})
print(response.text)

print("Update Record using add method..")
response=requests.put("http://localhost:8000/updateUser/",{"id":101,"Name":"Payal","City":"Baramati"})
print(response.text)

print("Delete Record using delete method..")
response=requests.delete("http://localhost:8000/deleteUser/Payal")
print(response.text)