import requests

res = requests.get('http://127.0.0.1:5000/api')

json = res.json()

print(json[0])
print(json[1])
print(json[2])
print(json[3])
print(json[4])
print(json[5])