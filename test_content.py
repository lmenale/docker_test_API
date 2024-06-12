import os
import requests

# Definition of the API address and port
api_address = 'api_container'
api_port = 8000

# Sentences and their expected sentiment
sentences = {
    'life is beautiful': "> 0",
    'that sucks': "< 0"
}

# Perform content tests
output = '''
============================
    Content test
============================
'''

for sentence, expected_sentiment in sentences.items():
    for version in ('v1', 'v2'):
        r = requests.get(
            url=f'http://{api_address}:{api_port}/{version}/sentiment',
            params={'username': 'alice', 'password': 'wonderland', 'sentence': sentence}
        )
        # sentiment_score = r.json().get('score', 0)
        sentiment_score = r.json()['score']
        test_status = 'SUCCESS' if (sentiment_score > 0) else 'FAILURE'
        sentiment_score = '> 0' if sentiment_score > 0 else '< 0'
        output += f'''
request done at "/{version}/sentiment"
| sentence="{sentence}"
| version="{version}"
expected sentiment = {expected_sentiment}
actual sentiment = {sentiment_score}
==>  {test_status}
'''

print(output)

# Log to file if LOG environment variable is set
if os.environ.get('LOG') == '1':
    with open('/logs/api_test.log', 'a') as file:
        file.write(output)
