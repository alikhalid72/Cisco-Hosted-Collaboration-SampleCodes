import urllib.request
import requests

u='alikh1234@yahoo.com'
p='zuzaali10'
url='https://api.github.com/users/username'



response = requests.get(url,
                        auth=requests.auth.HTTPBasicAuth(
                          'u',
                          'p'))
print (response.text)