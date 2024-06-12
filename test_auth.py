import os
import requests

# Definition of the API address and port
api_address = 'api_container'
api_port = 8000

# Users and passwords
credentials = [
    ('alice', 'wonderland', 200),
    ('bob', 'builder', 200),
    ('clementine', 'mandarine', 403)
]

# Perform authentication tests
output = '''
============================
    Authentication test
============================
'''

for username, password, expected_status in credentials:
    r = requests.get(
        url=f'http://{api_address}:{api_port}/permissions',
        params={'username': username, 'password': password}
    )
    status_code = r.status_code
    test_status = 'SUCCESS' if status_code == expected_status else 'FAILURE'
    output += f'''
request done at "/permissions"
| username="{username}"
| password="{password}"
expected result = {expected_status}
actual result = {status_code}
==>  {test_status}
'''

print(output)

# Log to file if LOG environment variable is set
if os.environ.get('LOG') == '1':
    with open('/logs/api_test.log', 'a') as file:
        file.write(output)
