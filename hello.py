import requests
print("hello")
x = requests.get('https://w3schools.com').text
print(x)
