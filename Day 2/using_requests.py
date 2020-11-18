import requests

url = 'https://jsonplaceholder.typicode.com'
param = 'users'
id = 3

full_path = f'{url}/{param}/{id}'

res = requests.get(full_path)

j = res.json()
print(j)

