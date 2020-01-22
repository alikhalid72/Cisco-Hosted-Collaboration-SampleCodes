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

#print(_credEncoded) # remove '#' to print the encoded credentials

url = "https://"+_ip+"/api/relation/HcsUserREL/" # This URI is to get users list

headers = {
    'authorization': 'Basic %s' % _credEncoded.decode("ascii"),
    'cache-control': "no-cache",
    "content-type": "application/json"
    }



#print(headers) # remove '#' to print the header

response = requests.request("GET", url, headers=headers,verify=False) # Requesting users info.
#print('resp1 cookies',response.cookies)

f= response.json() # Storing response data in json format.

with open('importeduser.json', 'w') as usersFile:
    json.dump(f, usersFile, indent=4)
for u in (f['resources']):
    _user_href = (u['meta']['references']['self'][0]['href'] )
    #_href = u['meta']['references']['self'][0]['href']  # Getting individual user's url
    #print(_user_href)
    _url2 = "https://"+_ip+_user_href
    response2 = requests.request("GET", _url2, cookies=response.cookies, verify=False)

    _userInfo = response2.json() # COnverting user's information into json format, and storing the data inside _userInfo variable.
    #print(_userInfo)
    _path = _userInfo['meta']['path']
    #print(_path)

    _putData = {
        "meta": {

            "path": [
                _path
            ]
        },

        "data": {

            "ps": {

                "entitlement_profile": "[\"DCloud-Bronze\", \"hcs.DCloudSP\"]"

            }

        }
    }

    response2 = requests.request("PATCH", _url2, headers=headers, cookies=response.cookies, data=json.dumps(_putData), verify=False)

    print(response2.text)
    #print('resp2 cookies',response2.cookies)

#_href = f['resources'][0]['meta']['references']['self'][0]['href'] # Getting individual user's url



# Setting the complete url for each user url, this url will provide the complete settings and features for the individual user
# this will be used to get and update each user's settings




# GET user's complete information:



#_data = _userInfo['data']['ps']['entitlement_profile']
_userInfo['data']['ps']['entitlement_profile']='["DCloud-Bronze", "hcs.DCloudSP"]'

_putData = {
    "meta": {

        "path": [
            _path
        ]
    },

    "data": {


        "ps": {

            "entitlement_profile": "[\"DCloud-Gold\", \"hcs.DCloudSP\"]"

        }

    }
}




#response2 = requests.request("PATCH", _url2, headers=headers,data=json.dumps(_putData), verify=False)

print(response2.text)
