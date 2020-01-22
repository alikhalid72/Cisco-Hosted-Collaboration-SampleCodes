import requests
import json
import sys
import base64


import cucdm_conf  # CUCDM information is in cucdm_config.py, including CUCDM IP address, Admin user name and password


requests.packages.urllib3.disable_warnings() # Disable certificate warning message

username = cucdm_conf.username # Username imported from cucdm_conf
password = cucdm_conf.password # Password imported from cucdm_conf
_ip = cucdm_conf.ip # IP address of the CUCDM server imported from cucdm_conf

_credentials = ('%s:%s' % (username, password)) # Credentials in a combined form 'username:password'

_credEncoded = base64.b64encode(_credentials.encode('ascii')) # Credentials to 64 based encoding before sending


def get_auth(uname=cucdm_conf.username,pword=_credEncoded,ip=cucdm_conf.ip):
    """
    This function make authentication against CUCDM server.
    Passing ip, version,username and password when use as standalone function to overwrite the configuration above.
    This function returns a new service ticket.
    """


    # url for the post ticket API request
    post_url = "https://"+ip+"/noninteractivelogin/"

    headers = {
        'authorization': 'Basic %s' % _credEncoded.decode("ascii"),
        'cache-control': "no-cache",
        "content-type": "application/json"
    }

    # POST request and response
    try:
        r = requests.post(post_url,headers=headers,verify=False) # Using 'verify=False' to ignore the self signed certification of the CUCDM server

        # To get response header information and store it in a new variable.
        # Response header includes XCSRFToken value for this session.
        jsonheader=r.headers


        # Remove # to pront all response header information:

        print(jsonheader)

        # Return XCSRFToken value:
        XCSRFToken=jsonheader['X-CSRFToken']
        return (XCSRFToken)


    except:
        # Something wrong, cannot get service ticket
        print ("Status: %s"%r.status_code)
        print ("Response: %s"%r.text)
        sys.exit ()

def getUsers(ip=cucdm_conf.ip,api='', params =''):
    """
    To simplify requests.get with default configuration.Return is the same as requests.get
    """

    _ref = "https:"+ip

    ticket = get_auth()

    headers = {"content-type": "application/json",'csrftoken':ticket}

    url = "https://"+ip+"/api/"+api
    print ("\nExecuting GET '%s'\n"%url)
    try:
    # The request and response of "GET /network-device" API
        resp= requests.get('https://198.18.133.254/api/relation/HcsUserREL/', headers=headers,verify = False)
        #return(resp)
        print(resp.text)






        #print(f)
        #putchange=requests.put('https://198.18.133.254/api/relation/HcsUserREL/599f3fedacba0ae6b441121b/?hierarchy=551cbc26acba0a1691197134&policy_name=HcsUserRelFDP',data=json.dumps(f), headers=headers, verify=False)
        #print(putchange.text)

    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
        sys.exit()




def post(ip=cucdm_conf.ip,ver=cucdm_conf.version,uname=cucdm_conf.username,pword=cucdm_conf.password,api='',data=''):
    """
    To simplify requests.post with default configuration.Return is the same as requests.post
    """
    ticket = get_X_auth_token()
    headers = {"content-type" : "application/json","X-Auth-Token": ticket}
    url = "https://"+ip+"/api/"+ver+"/"+api
    print ("\nExecuting POST '%s'\n"%url)
    try:
    # The request and response of "POST /network-device" API
        resp= requests.post(url,json.dumps(data),headers=headers,verify = False)
        return(resp)
    except:
       print ("Something wrong to POST /",api)
       sys.exit()

def put(ip=cucdm_conf.ip,ver=cucdm_conf.version,uname=cucdm_conf.username,pword=cucdm_conf.password,api='',data=''):
    """
    To simplify requests.put with default configuration.Return is the same as requests.put
    """
    ticket = get_X_auth_token()
    headers = {"content-type" : "application/json","X-Auth-Token": ticket}
    url = "https://"+ip+"/api/"+ver+"/"+api
    print ("\nExecuting PUT '%s'\n"%url)
    try:
    # The request and response of "PUT /network-device" API
        resp= requests.put(url,json.dumps(data),headers=headers,verify = False)
        return(resp)
    except:
       print ("Something wrong to PUT /",api)
       sys.exit()

def delete(ip=cucdm_conf.ip,ver=cucdm_conf.version,uname=cucdm_conf.username,pword=cucdm_conf.password,api='',params=''):
    """
    To simplify requests.delete with default configuration.Return is the same as requests.delete
    """
    ticket = get_X_auth_token()
    headers = {"X-Auth-Token": ticket,'content-type': 'application/json'}
    url = "https://"+ip+"/api/"+ver+"/"+api
    print ("\nExecuting DELETE '%s'\n"%url)
    try:
    # The request and response of "DELETE /network-device" API
        resp= requests.delete(url,headers=headers,params=params,verify = False)
        return(resp)
    except:
       print ("Something wrong to DELETE /",api)
       sys.exit()
get()