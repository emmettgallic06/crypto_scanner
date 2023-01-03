import polygonscan
import pandas as pd
from datetime import datetime

APIKEY = "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83"
address = "0x49380ad3caf5baabc09ad296703c0a847fcb122e"

data = {'hash': [],
        'time': []}

with polygonscan.PolygonScan(APIKEY, False) as matic:
    f = matic.get_normal_txs_by_address(address=address, startblock=0, endblock=37625559, sort="asc")

    # Add hash to df
    for i in range(0,len(f)):
        data['hash'].append(f[i]['hash'])
    # Convert time of hash into time and add to df
    for i in range(0,len(f)):
        data['time'].append(datetime.fromtimestamp(int(f[i]['timeStamp'])))



df = pd.DataFrame(data)

print(df)
