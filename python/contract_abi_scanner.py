from polygonscan import PolygonScan
import pandas as pd
from json import loads

APIKEY = "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83"
data = [{'name': [],
         'type': []}]

with PolygonScan(APIKEY, False) as matic:
    datab = loads(matic.get_contract_abi(address='0xEDcFb6984a3c70501BAA8b7f5421Ae795ecC1496'))
    df_schema = pd.DataFrame(datab)
    column_headers = pd.DataFrame(list(df_schema.columns.values))
    print(column_headers)


def get_ca_abi(ca):
    with PolygonScan(APIKEY, False) as matic:
        return loads(matic.get_contract_abi(address=ca))


def get_ca_functions(ca):
    with PolygonScan(APIKEY, False) as matic:
        f = get_ca_abi(ca)
        for i in f[0]['input']:
            data['name'].append(f[i]['name'])
        for i in range(0, len(f)):
            data['type'].append(f[i]['type'])
    df = pd.DataFrame(data)
    df = pd.DataFrame(data)
    df.set_index('hash', inplace=True)
    return df

x = get_ca_abi('0xEDcFb6984a3c70501BAA8b7f5421Ae795ecC1496')
print(x)
print(get_ca_functions('0xEDcFb6984a3c70501BAA8b7f5421Ae795ecC1496'))
