import polygonscan
import pandas as pd
import datetime

time = str(datetime.datetime.now() - datetime.timedelta(seconds = 84))
current_time = str(int(datetime.datetime.now().timestamp()-84))
APIKEY = "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83"
address = "0x49380ad3caf5baabc09ad296703c0a847fcb122e"
data = {'Address':[address],
        'Timestamp': [],
        'Amount': [],
        'Time': []}

with polygonscan.PolygonScan(APIKEY, False) as matic:
    # Grab Amount
    data['Amount'].append(matic.get_matic_balance(address=address))

    # Grab TimeStamp
    data['Timestamp'].append(matic.get_block_number_by_timestamp(timestamp=current_time, closest="before"))

    # Add converted Time
    data['Time'].append(time)

# Convert to Pandas Dataframe
df = pd.DataFrame(data)

# Convert to CSV File
df.to_csv('../output/results.csv', index= False, header=True)
print(matic.get_normal_txs_by_address(address=address, startblock=0, endblock=37625559, sort="asc"))
# print(polygonscan.get_normal_txs_by_address(address))
# matic.get_normal_txs_by_address()
