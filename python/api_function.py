import requests
import json
from datetime import datetime

def block_number_by_timestamp(timestamp,when):
    parameters ={
    "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
    "module": "block",
    "action": "getblocknobytime",
    "timestamp": timestamp,
    "closest":when,
    }
    response = requests.get("https://api.polygonscan.com/api", params=parameters)
    return response.json()['result']

def normal_transactions_by_address(address,start,end):
     st = datetime.strptime(start, '%Y-%m-%dT%H:%M')
     stts = str(int(datetime.timestamp(st)))
     en = datetime.strptime(end, '%Y-%m-%dT%H:%M')
     ents = str(int(datetime.timestamp(en)))
     parameters ={
    "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
    "module": "account",
    "action": "txlist",
    "address": address,
    "startblock": block_number_by_timestamp(stts,'after'),
    "endblock": block_number_by_timestamp(ents, 'before'),
    "sort": "asc"
     }
     response = requests.get("https://api.polygonscan.com/api", params=parameters)
     return response.json()

# 2023-01-17T20:14
# temp = normal_transactions_by_address("0x4c6348bf16FeA56F3DE86553c0653b817bca799A","2023-01-10T20:14","2023-01-17T20:14")
# # temp = block_number_by_timestamp("1673317946000",'before')
# print(temp)