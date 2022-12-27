from polygonscan import PolygonScan
import pandas as pd
import numpy as np
import csv

APIKEY = "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83"
address = "0x02F70172F7f490653665C9bFAc0666147c8aF1F5"
data = []

with PolygonScan(APIKEY,False) as matic:
    data.append(matic.get_matic_balance(address=address))

df = pd.DataFrame(data)
df.to_csv('../output/results.csv', index= False, header=False)