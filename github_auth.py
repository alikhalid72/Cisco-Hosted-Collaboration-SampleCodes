import requests

from requests.auth import HTTPBasicAuth

_user ='DCloudSPAdmin@dcloud.cisco.com'
_pass = 'C1sco123'

_url= 'http://198.18.133.254/login'
responce = requests.get(url=_url, auth=HTTPBasicAuth(_user, _pass),headers={"Referer":"http://198.18.133.254/login"}, verify=False)

print (responce.text)