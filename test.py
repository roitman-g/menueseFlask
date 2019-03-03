import requests




method = "PO"

if method == "GET":
    result = requests.get('http://localhost:5000/restaurants/')
else:
    result = requests.post('http://localhost:5000/restaurants/', data = {'name': 'Ichiban', 'description': 'Just some asian restaurant'})


print(result)
print(result.json())