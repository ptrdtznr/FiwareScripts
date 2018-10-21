__author__ = "Peter Detzner" 
__maintainer__ = "Peter Detzner"
__version__ = "0.0.1a"
__status__ = "Developement"

 
import requests


# local imports
import globals 
from configParser import Config
from contextbrokerhandler import ContextBrokerHandler

HOST = '0.0.0.0'
PORT = 5555
NGSI_VERSION_V2 = "v2"
OCB_SERVER_ADDRESS = "localhost"
OCB_POST = "1026"

SUBSCRIPTIONS = "subscriptions"
ENTITIES = "entities"

def getOcbAddress(specific = ""):
    return "http://" + OCB_SERVER_ADDRESS + ":" + OCB_POST + "/" + NGSI_VERSION_V2 + "/" + specific+ "/"

 
def deleteSubscription(id):
    try:
        print "Deleting " + id
        print getOcbAddress(SUBSCRIPTIONS)+ id
        response = requests.request("DELETE", getOcbAddress(SUBSCRIPTIONS)+ id)  
        if(response.status_code // 200 == 1):
            print "Success"
    except expression as Exception:
        print "Failed"
        return False

    return True

def deleteAllSubscriptions():
    response = requests.request("GET", getOcbAddress(SUBSCRIPTIONS))  
    if(response.status_code // 200 == 1):
        for item in response.json():
            deleteSubscription(item['id'])
        
deleteAllSubscriptions()