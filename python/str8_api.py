import requests
import json

def get_data(api):
    response = requests.get(f"{api}")
    if response.status_code == 200:
        print("sucessfully fetched the data")
        return formatted_print(response.json())
    else:
        print(
            f"Hello person, there's a {response.status_code} error with your request")

def get_user_data(api, parameters):
    response = requests.get(f"{api}", params=parameters)
    if response.status_code == 200:
        print("sucessfully fetched the data with parameters provided")
        return formatted_print(response.json())
    else:
        print(
            f"Hello person, there's a {response.status_code} error with your request")

def formatted_print( obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

parameters = {
    "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
    "module": "account",
    "action": "txlist",
    "address": "0x5A534988535cf27a70e74dFfe299D06486f185B7"
}


api_call = get_user_data("https://api.polygonscan.com/api",parameters)
print(api_call)