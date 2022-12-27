from polygonscan import PolygonScan
import pandas as pd

APIKEY = "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83"
address = "0x02F70172F7f490653665C9bFAc0666147c8aF1F5"
data = []

with PolygonScan(APIKEY,False) as matic:
    # Grab Amount
    data.append(matic.get_matic_balance(address=address))

    # Grab TimeStamp
    data.append(matic.get_block_number_by_timestamp(timestamp="1671949596", closest="before"))

# Convert to Pandas Dataframe
df = pd.DataFrame(data)

# Convert to CSV File
df.to_csv('../output/results.csv', index= False, header=False)