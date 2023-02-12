#######################################################################
################ Tutorial API Call with Authentication ################
###########https://www.dataquest.io/blog/last-fm-api-python/###########
#######################################################################

import requests
import json

API_KEY = '*****************************'
USER_AGENT = '***************'

#headers = {
#    'user-agent': USER_AGENT
#}

#payload = {
#    'api_key': API_KEY,
#    'method': 'chart.gettopartists',
#    'format': 'json'
#}

#r = requests.get('https://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
#print(r.status_code)


def lastfm_get(payload):
    # define headers and URL
    headers = {'user-agent': USER_AGENT}
    url = 'https://ws.audioscrobbler.com/2.0/'

    # Add API key and format to the payload
    payload['api_key'] = API_KEY
    payload['format'] = 'json'
    #payload['method'] = 'chart.gettopartists'

    response = requests.get(url, headers=headers, params=payload)
    return response

#r = lastfm_get(payload)
r = lastfm_get({'method': 'chart.gettopartists'})
#print(r.status_code)


def jsonPrint(jsonObj):
    output = json.dumps(jsonObj, sort_keys=True, indent=2)
    print(output)

#jsonPrint(r.json())
jsonPrint(r.json()['artists']['@attr'])