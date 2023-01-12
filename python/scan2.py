import polygonscan
import pandas as pd
from datetime import datetime

APIKEY = "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83"
add = "0x4c6348bf16FeA56F3DE86553c0653b817bca799A"

data = {'hash': [],
        'time': [],
        'value': []}

def ts_time_switch(var):
    return datetime.fromtimestamp(int(var))

def get_hash_time(address, methodId):
    with polygonscan.PolygonScan(APIKEY, False) as matic:
        f = matic.get_normal_txs_by_address(address=address, startblock=0, endblock=37625559, sort="asc")
        print(f[2]['methodId'])
        # Add hash to df
        for i in range(0,len(f)):
            if f[i]['methodId'] == methodId:
                data['hash'].append(f[i]['hash'])
        for i in range(0, len(f)):
            if f[i]['methodId'] == methodId:
                data['value'].append(f[i]['value'])
        # Convert time of hash into time and add to df
        for i in range(0,len(f)):
            if f[i]['methodId'] == methodId:
                data['time'].append(ts_time_switch(f[i]['timeStamp']))

get_hash_time(add, '0x')

df = pd.DataFrame(data)
df.set_index('hash', inplace=True)

print(df)

with polygonscan.PolygonScan(APIKEY, False) as matic:
    datab = matic.get_normal_txs_by_address(address=add, startblock=0, endblock=37625559, sort="asc")
    df_schema = pd.DataFrame(datab)
    column_headers = pd.DataFrame(list(df_schema.columns.values))

    ## print("The Column headers :", column_headers)