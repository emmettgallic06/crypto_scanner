import requests
import json


class MakeApiCall:

    def get_data(self, api):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            print("sucessfully fetched the data")
            self.formatted_print(response.json())
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")

    def get_user_data(self, api, parameters):
        response = requests.get(f"{api}", params=parameters)
        if response.status_code == 200:
            print("sucessfully fetched the data with parameters provided")
            self.formatted_print(response.json())
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")

    def formatted_print(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def __init__(self, api):
        # self.get_data(api)

        parameters = {
            "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
            "module": "account",
            "action": "txlist",
            "address": "0x5A534988535cf27a70e74dFfe299D06486f185B7"
        }

        self.get_user_data(api, parameters)


if __name__ == "__main__":
    api_call = MakeApiCall("https://api.polygonscan.com/api")