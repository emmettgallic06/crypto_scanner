import requests
import json
from datetime import datetime

import str8_api

def block_number_by_timestamp(timestamp,):
    parameters ={
    "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
    "module": "block",
    "action": "getblocknobytime",
    "timestamp": timestamp,
    "closests":"before",
    }
    response = requests.get("https://api.polygonscan.com/api", params=parameters)
    return response

def normal_transactions_by_address(address,start,end):
     st = datetime.strptime(start, '%Y-%m-%dT%H:%M')
     stts = datetime.timestamp(st)
     en = datetime.strptime(end, '%Y-%m-%dT%H:%M')
     ents =datetime.timestamp(en)
     parameters ={
    "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
    "module": "account",
    "action": "txlist",
    "address": address,
    "startblock": block_number_by_timestamp(stts),
    "endblock": block_number_by_timestamp(ents),
    "sort": "asc"
     }
     response = requests.get("https://api.polygonscan.com/api", params=parameters)
     return response.json()