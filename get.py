from cucdm_auth import *

try:
    resp = get(api="policy/tag")
    status = resp.status_code
    print("status: ",status)
    print ("Response:",json.dumps(resp.json(),indent=4))
except:
    print ("Something wrong with GET /policy/tag !")
