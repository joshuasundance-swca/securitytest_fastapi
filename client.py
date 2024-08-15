import requests

from keys import correct_key, incorrect_key

url = "http://localhost:8081/protected-endpoint"


api_key_name = "access-token"

correct_headers = {api_key_name: correct_key}

incorrect_headers = {api_key_name: incorrect_key}

print("Trying with correct key:")

response = requests.get(url, headers=correct_headers)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")

print()

print("Trying with incorrect key:")

response_2 = requests.get(url, headers=incorrect_headers)

print(f"Status Code: {response_2.status_code}")
print(f"Response: {response_2.json()}")
