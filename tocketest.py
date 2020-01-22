import requests
import json
import base64
import cucdm_conf

requests.packages.urllib3.disable_warnings() # Disable warning message

username = cucdm_conf.username # Username imported from cucdm_conf
password = cucdm_conf.password # Password imported from cucdm_conf
_ip = cucdm_conf.ip # IP address of the CUCDM server imported from cucdm_conf

_credentials = ('%s:%s' % (username, password)) # Credentials in a combined form 'username:password'

_credEncoded = base64.b64encode(_credentials.encode('ascii')) # Credentials to 64 based encoding before sending


print(_credEncoded.decode('ascii')) # remove '#' to print the encoded credentials

url = "https://"+_ip+"/api/relation/HcsUserREL/" # This URI is to get users list


headers = {
    'authorization': 'Basic %s' % _credEncoded.decode("ascii"),
    "content-type": "application/json"
    }

headers1 = {
    'Authorization': "Basic RENsb3VkU1BBZG1pbkBkY2xvdWQuY2lzY28uY29tOkMxc2NvMTIz",
    'Cache-Control': "no-cache",
    'Postman-Token': "f5163695-fbed-42ab-90c9-967eb6f20049"
    }
#print(headers) # remove '#' to print the header

response = requests.request("GET", url,headers=headers,verify=False) # Requesting users info.
hdr = response.headers
jjj = hdr.get('Set-Cookie')
kkk = jjj.split(';')
_csrftoken = kkk[0]
_SID = kkk[3]
_SessID = _SID.split(',')
_SessionID = _SessID[1]
print(response.status_code)
print(_csrftoken)

respCookies = response.cookies
print('Resp cookies', respCookies)
_cookies = _SessionID+','+_csrftoken+','+'sso_Connection: keep-alive'

print(_cookies)
_subs_url = "https://198.18.133.254/api/relation/HcsUserREL/" # This url is to get subscribers list

headers2 = {"content-type": "application/json"}

response2 = requests.request("GET", _subs_url, headers=headers2, cookies=response.cookies,  verify=False)
_subs_list= response2.text
print('rep2',response2.status_code)
print('resp2 contents=',_subs_list)