import json


def get_users_info():
    with open('users.json') as users_data:  #open users JSON file
        udata = json.load(users_data)
        for u in (udata['resources']):
            uid= u['data']['username']
            print ('User ID:',uid)
            try:
                print ('Entitlement Profile:', u['data']['ps']['entitlement_profile'])
                global _EP
                _EP=str(u['data']['ps']['entitlement_profile'])
                global _EPlist
                global _EPname
                global _EPhierarchy
                _EPlist=_EP.split(",")
                _EPname= _EPlist[0]
                _EPhierarchy=_EPlist[1]
                #get_entitlment_features(_EPname)
                get_subs_features(uid)







            except KeyError:
                print('-- No Entitlement Profile associated in the CUCDM --')


def get_subs_features(userid):
    with open('subs.json') as subs_data:
        data = json.load(subs_data)
        nfn = 'new.json'
        for r in (data['resources']):
            _uid= str(r['data']['userid'])
            _uname=str(userid)
            #global imp
            #global emcc
            #global mobility
            #global snr
            #global _vm

            if _uid==_uname:
                imp = str(r['data']['imAndPresenceEnable'])
                mobility = r['data']['enableMobility']
                emcc = r['data']['enableEmcc']
                _vm = r['data']['CUCUser'][0]['IsSetForVmEnrollment']






                print('imp:',imp,'mobility:',mobility,'emcc:',emcc,'VM:',_vm)

    subs_data.close()







def get_entitlment_features(ep):
    with open('ent.json') as entitl:    #open JSON file of Entitlement Prifile list configured in CUCDM
        ent = json.load(entitl)
        print (ep)

        #print('')
        #print ('----Entitlement list in CUCDM-----')
        for e in (ent['resources']):
            ename= e['data']['name']
            global eprofile
            global _extension_m
            global _presence
            global _voicemil
            global _num_devices
            global _voice
            global _snr



            if ename in ep:

                _extension_m= e['data']['extension_mobility']
                _presence= e['data']['presence']
                _voicemil = e['data']['voicemail']
                _num_devices = e['data']['num_devices']
                _voice = e['data']['voice']
                _snr = e['data']['snr']


                eprofile = {'extension_mobility':e['data']['extension_mobility'],'presence': e['data']['presence'],'voicemail': e['data']['voicemail'],'num_devices': e['data']['num_devices'],'voice':e['data']['voice'],'snr':e['data']['snr']  }
                print (eprofile)

            #print ename
            #print 'Features:-',eprofile



get_users_info()