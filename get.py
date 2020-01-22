from cucdm_auth import * # APIC-EM IP is assigned in apicem_config.py

try:
    resp = get(api="policy/tag")
    status = resp.status_code
    print("status: ",status)
    print ("Response:",json.dumps(resp.json(),indent=4))
except:
    print ("Something wrong with GET /policy/tag !")
