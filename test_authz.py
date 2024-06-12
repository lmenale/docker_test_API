import os
import requests

# Definition of the API address and port
api_address = 'api_container'
api_port = 8000

# Users and their access rights
users = {
    'alice': ('wonderland', True, True),
    'bob': ('builder', True, False)
}

# Sentiment sentences
sentence = "hello world"

# Perform authorization tests
output = '''
============================
    Authorization test
============================
'''

for username, (password, access_v1, access_v2) in users.items():
    for version in ('v1', 'v2'):
        expected_status = 200 if (version == 'v1' and access_v1) or (version == 'v2' and access_v2) else 403
        r = requests.get(
            url=f'http://{api_address}:{api_port}/{version}/sentiment',
            params={'username': username, 'password': password, 'sentence': sentence}
        )
        status_code = r.status_code
        test_status = 'SUCCESS' if status_code == expected_status else 'FAILURE'
        output += f'''
request done at "/{version}/sentiment"
| username="{username}"
| password="{password}"
| sentence="{sentence}"
| version="{version}"
expected result = {expected_status}
actual result = {status_code}
==>  {test_status}
'''

print(output)

# Log to file if LOG environment variable is set
if os.environ.get('LOG') == '1':
    with open('/logs/api_test.log', 'a') as file:
        file.write(output)
