import requests 
data = requests.post("http://192.168.50.247:5690/user_accountreq",json={"first_name":"Marvin","last_name":"Gays","emails":"marvin380@hotmail.com","password":"Rkjl3548123#","address":"usa"})
print(data.json())
