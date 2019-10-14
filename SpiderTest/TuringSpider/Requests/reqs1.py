import requests

params1 = {
    'name': 'laosi',
    'age': '35'
}
r = requests.get('http://httpbin.org/get', params=params1)
print(r.text)
