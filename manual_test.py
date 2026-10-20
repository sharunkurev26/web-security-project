'''import requests

BASE_URL = 'http://127.0.0.1:5000'

print('--- MANUAL TESTING TOOL ---')

# 1. Test registering a custom username and password
custom_user = input('Enter a new username to register: ')
custom_pass = input('Enter a password: ')

reg_res = requests.post(
    f'{BASE_URL}/register',
    json={'username': custom_user, 'password': custom_pass},
)
print('Registration Result:', reg_res.json())

# 2. Test logging in with those credentials
print('\nAttempting Login...')
login_res = requests.post(
    f'{BASE_URL}/login',
    json={'username': custom_user, 'password': custom_pass},
)
print('Login Result:', login_res.json())

# 3. Test a SQL Injection Attack!
print('\n--- TESTING SQL INJECTION DEFENSE ---')
# Hackers try to use SQL syntax to bypass logins: ' OR '1'='1
sqli_payload = {'username': "' OR '1'='1", 'password': 'fake_password'}

attack_res = requests.post(f'{BASE_URL}/login', json=sqli_payload)
print('SQL Injection Status Code:', attack_res.status_code)
print('SQL Injection Server Response:', attack_res.json())'''

'''import requests

BASE_URL = 'http://127.0.0.1:5000'

print('--- INTERACTIVE HACKER TESTER ---')
print('Try typing different SQL Injection payloads to see if you can break in!')
print("Example payload to try: ' OR '1'='1\n")

# Let YOU type the hacking input
attack_user = input('Enter username payload: ')
attack_pass = input('Enter password payload: ')

print(f"\n[Sending attack...] Username: {attack_user} | Password: {attack_pass}")

res = requests.post(
    f'{BASE_URL}/login', json={'username': attack_user, 'password': attack_pass}
)

print('\n--- SERVER REACTION ---')
print('Status Code:', res.status_code)
print('Response:', res.json())'''


import requests

BASE_URL = 'http://127.0.0.1:5000'

print('--- INTERACTIVE MANUAL TESTING LAB ---')

# Step 1: Register a real user manually
print('\n[Step 1: Register a new account]')
reg_user = input('Choose a username to register: ')
reg_pass = input('Choose a password: ')

reg_res = requests.post(
    f'{BASE_URL}/register', json={'username': reg_user, 'password': reg_pass}
)
print('Registration Response:', reg_res.json())

# Step 2: Test logging in with those correct credentials
print('\n[Step 2: Test login with correct credentials]')
login_user = input('Enter username to log in: ')
login_pass = input('Enter password to log in: ')

login_res = requests.post(
    f'{BASE_URL}/login',
    json={'username': login_user, 'password': login_pass},
)
print('Login Status Code:', login_res.status_code)
print('Login Response:', login_res.json())

# Step 3: Test SQL Injection or bad inputs
print('\n[Step 3: Test a hacking payload or wrong password]')
attack_user = input('Enter a hacking payload or wrong username: ')
attack_pass = input('Enter password: ')

attack_res = requests.post(
    f'{BASE_URL}/login',
    json={'username': attack_user, 'password': attack_pass},
)
print('Attack Status Code:', attack_res.status_code)
print('Attack Response:', attack_res.json())
