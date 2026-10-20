import requests

BASE_URL = 'http://127.0.0.1:5000'

print('1. Testing Home Route...')
res = requests.get(f'{BASE_URL}/')
print(res.json())

print('\n2. Registering a New User...')
reg_data = {'username': 'cyber_student', 'password': 'SuperSecretPassword123'}
res = requests.post(f'{BASE_URL}/register', json=reg_data)
print(res.json())

print('\n3. Logging In...')
res = requests.post(f'{BASE_URL}/login', json=reg_data)
data = res.json()
print(data)

if 'access_token' in data:
  token = data['access_token']
  print('\n4. Accessing Protected Dashboard with JWT...')
  headers = {'Authorization': f'Bearer {token}'}
  res = requests.get(f'{BASE_URL}/dashboard', headers=headers)
  print(res.json())