  
import urllib.request
import requests

u='Username'
p='password'
url='https://api.github.com/users/username'



response = requests.get(url,
                        auth=requests.auth.HTTPBasicAuth(
                          'u',
                          'p'))
print (response.text)
