import requests
import json
import base64
import cucdm_conf
#import postmancode
requests.packages.urllib3.disable_warnings() # Disable warning message

username = cucdm_conf.username # Username imported from cucdm_conf
password = cucdm_conf.password # Password imported from cucdm_conf
_ip = cucdm_conf.ip # IP address of the CUCDM server imported from cucdm_conf

_credentials = ('%s:%s' % (username, password)) # Credentials in a combined form 'username:password'

_credEncoded = base64.b64encode(_credentials.encode('ascii')) # Credentials to 64 based encoding before sending


#print(_credEncoded)

_subs_url = "https://"+_ip+"/api/relation/Subscriber/" # This url is to get subscribers list



headers = {
    'authorization': 'Basic %s' % _credEncoded.decode("ascii"),
    'cache-control': "no-cache",
    "content-type": "application/json"
    }
#print(headers)

response = requests.request("GET", _subs_url, headers=headers,verify=False) # Requesting all subscribers info.

_subs_list= response.json() # Storing response data in json format.

print(response.cookies)
with open('importeduser.json') as users_data:  #open users JSON file
        udata = json.load(users_data)

def findUser(_userid):
        for u in (udata['resources']):
            uid= u['data']['username']
            if uid == _userid:

                print ('User ID:',uid)


for s in (_subs_list['resources']):
    _subs_href = (s['meta']['references']['self'][0]['href'] )
    #_href = u['meta']['references']['self'][0]['href']  # Getting individual user's url
    print('Subscriber href',_subs_href)
    _userid = (s['data']['userid'])
    print('User ID in subs list',_userid)
    findUser(_userid)
    _url2 = "https://"+_ip+_subs_href
    response2 = requests.request("GET", _url2, cookies=response.cookies, verify=False)

    _subsInfo = response2.json() # COnverting user's information into json format, and storing the data inside _userInfo variable.
    #print(_subsInfo)
    _path = _subsInfo['meta']['path']
    print('Subscriber path',_path)


with open('EntProfiles.json') as EP:
    _EP_data = json.load(EP)

def comp_ent():
    for e in _EP_data['resources']:
        _EM = (e['data']['extension_mobility'])
        _IMP = (e['data']['presence'])
        _VM = (e['data']['voicemail'])
        _Num_of_Dev = (e['data']['num_devices'])
        _EP_name = (e['data']['name'])
        _EP_hierarchy = (e['meta']['hierarchy'])
        _EntProfile = ("["+_EP_name+","+ _EP_hierarchy+"]")
        print(_EntProfile)



#comp_ent()
