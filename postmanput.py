import requests

url = "https://198.18.133.254/api/relation/HcsUserREL/599f3fedacba0ae6b441121b/"

def putEntitlement(path,entitlemetProfile):
    payload = "{\n    \"meta\": {\n       \n        \"path\": [\n            \"1c0ffee2c0deab00da595101\",\n            \"545ab6b5acba0a18a0d3a86e\",\n            \"551cbc26acba0a1691197134\",\n            \"551cc09bacba0a1691197285\",\n            \"551dbc29acba0a169119a44e\",\n            \"599f3fedacba0ae6b441121b\"\n        ]\n    },\n    \n    \"data\": {\n        \n        \n        \"ps\": {\n            \n            \"entitlement_profile\": \"[\\\"DCloud-Gold\\\", \\\"hcs.DCloudSP\\\"]\"\n            \n        }\n       \n    }\n}"
    headers = {
        'content-type': "application/json",
        'authorization': "Basic '64encodedauth'",
        'cache-control': "no-cache",
        'postman-token': "8c0b428b-da7e-c9ae-540c-07556411dd43"
        }

    response = requests.request("PATCH", url, data=payload, headers=headers, verify=False)

    print(response.text)

putEntitlement()
