import json
import requests

def get_json():
    url = 'http://iot.dis.eafit.edu.co/Thingworx/Things/ruteadora3ejes_thing/Services/QueryPropertyHistory?method=post'
    headers = {'appKey': '09001afb-37e7-4fef-b32a-070480968a0a',
            'Accept': 'application/json'}

    getreq = requests.get(url, headers=headers).json()
    return getreq
