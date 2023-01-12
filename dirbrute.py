import requests
 
response = requests.get("http://g1.com.br")
print(response.status_code)