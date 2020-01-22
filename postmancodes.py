import requests
import json

url = "https://198.18.133.254/api/relation/HcsUserREL/"

headers = {
    'authorization': "Basic aGNzYWRtaW46QyFzYzAxMjM=",
    'content-type': "application/json"
    }


r = requests.get(url, headers=headers, verify=False)
    # remove '#' if need to print out response
    # print (r.text)

    # return service ticket
jsonresp=r.text
f = json.loads(jsonresp)
#print(json.dumps(f, indent=5, sort_keys=True))

print(f)
print(jsonresp)
for u in (f['resources']):
    uid = u['data']['username']
    print('User ID:'), uid
    try:
        print('Entitlement Profile:'), u['data']['ps']['entitlement_profile']

    except KeyError:
        print('--No Entitlement Profile associated in CUCDM --')

