__author__ = "ptrdtznr"
__status__ = "Dev"

# gobal imports

import requests
import httplib


# local imports
import ocb

def deleteSubscription(id):
    try:
        print "Deleting " + id 
        response = requests.request("DELETE", ocb.getOcbAddress(ocb.SUBSCRIPTIONS)+ id)  
        if(response.status_code // httplib.OK == 1):
            print "Success"
    except expression as Exception:
        print "Failed"
        return False

    return True

def deleteAllSubscriptions():
    response = requests.request("GET", ocb.getOcbAddress(ocb.SUBSCRIPTIONS))  
    if(response.status_code // httplib.OK == 1):
        for item in response.json():
            deleteSubscription(item['id'])
        
deleteAllSubscriptions()