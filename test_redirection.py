import requests

host = 'https://onetwotrip.com/'

response = requests.get(host, allow_redirects=False)
url = response.headers['Location']
assert ('https://www.onetwotrip.com/' == url)
print('test_redirection - ok')
