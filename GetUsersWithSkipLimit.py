import requests
import json
import sys
import sqlite3

requests.packages.urllib3.disable_warnings()  # Disable warning message


url = "https://198.18.133.254/api/relation/HcsUserREL/"



headers = {
    'Authorization': "Basic RENsb3VkU1BBZG1pbkBkY2xvdWQuY2lzY28uY29tOkMxc2NvMTIz",
    'Cache-Control': "no-cache",
    'Postman-Token': "953e9c63-e753-40de-93b3-ee6d09eb6400"
    }

##print(response.text)


conn = sqlite3.connect('sqlite_file.db')
c = conn.cursor()

c.execute('''CREATE TABLE if not exists usersdata
           (ID INTEGER PRIMARY KEY NULL,
           username           TEXT    NOT NULL,
           EP           TEXT);''')


querystring = {"skip": "0", "limit" : "100"}
try:
    response = requests.request("GET", url, headers=headers, params=querystring, verify=False)
except requests.exceptions.RequestException as _err:
        print ( "Error processing API request", _err )
        sys.exit(1)


usersJSONdump = response.json()

for u in (usersJSONdump['resources']):
    _user_href = (u['meta']['references']['self'][0]['href'] )
    _url2 = "https://198.18.133.254" + _user_href
    response2 = requests.request("GET", _url2, cookies=response.cookies, verify=False)
    userInfo = response2.json()
    _EP = (userInfo['data']['ps']['entitlement_profile'])
    _username = (userInfo['data']['username'])
    print(_username)
    print(_EP)

    c.execute("insert into usersdata (username, EP)  values (?,?)", (_username, _EP))
    c.close()



c.execute('SELECT * FROM usersdata ')
print(c.fetchall())

#with open('importedusers_by_API.json', 'a') as usersFile:
   #json.dump(usersJSONdump, usersFile, indent=4)