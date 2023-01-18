import requests
import json
from datetime import datetime

# Accounts
# - Get MATIC Balance for a Single Address
def get_matic_balance_single(address):
    parameters ={
    "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
    "module": "account",
    "action": "balance",
    "address": address
    }
    response = requests.get("https://api.polygonscan.com/api", params=parameters)
    return response.json()['result']

# - Get MATIC Balance for Multiple Addresses in a Single Call
def get_matic_balance_multiple(addresses):
    add_query = ""
    for i in addresses:
        add_query += i
    parameters ={
    "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
    "module": "account",
    "action": "balancemulti",
    "address": add_query
    }
    response = requests.get("https://api.polygonscan.com/api", params=parameters)
    return response.json()['result']

# - Get Historical MATIC Balance for a Single Address by BlockNo
def get_hist_data_balance_matic_single_block(address,block):

    parameters ={
    "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
    "module": "account",
    "action": "balancehistory",
    "address": address,
    "block": block
    }
    response = requests.get("https://api.polygonscan.com/api", params=parameters)
    return response.json()['result']

# Get a list of 'Normal' Transactions By Address
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

# Get a list of 'Internal' Transactions by Address
def internal_transactions_by_address(address, start, end):
    st = datetime.strptime(start, '%Y-%m-%dT%H:%M')
    stts = str(int(datetime.timestamp(st)))
    en = datetime.strptime(end, '%Y-%m-%dT%H:%M')
    ents = str(int(datetime.timestamp(en)))
    parameters = {
        "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
        "module": "account",
        "action": "txlistinternal",
        "address": address,
        "startblock": block_number_by_timestamp(stts, 'after'),
        "endblock": block_number_by_timestamp(ents, 'before'),
        "sort": "asc"
    }
    response = requests.get("https://api.polygonscan.com/api", params=parameters)
    return response.json()

# Get 'Internal Transactions' by Transaction Hash
def internal_transactions_by_hash(hash):
    parameters = {
        "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
        "module": "account",
        "action": "txlistinternal",
        "txhash": hash
    }
    response = requests.get("https://api.polygonscan.com/api", params=parameters)
    return response.json()

# Get 'Internal Transactions' by Block Range
def internal_transactions_by_block_range(startBlock,endBlock):
    parameters = {
        "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
        "module": "account",
        "action": "txlistinternal",
        "startblock": startBlock,
        "endblock": endBlock,
        "sort": "asc"
    }
    response = requests.get("https://api.polygonscan.com/api", params=parameters)
    return response.json()

# Get a list of 'ERC-20 Token Transfer Events' by Address
def get_list_erc20_events_by_address(contract, address, start, end):
    parameters = {
        "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
        "module": "account",
        "action": "tokentx",
        "contract": contract,
        "address": address,
        "startblock": start,
        "endblock": end,
        "sort": "asc"
    }
    response = requests.get("https://api.polygonscan.com/api", params=parameters)
    return response.json()

# Get a list of 'ERC-721 Token Transfer Events' by Address
def get_list_erc71_events_by_address(contract, address, start, end):
    parameters = {
        "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
        "module": "account",
        "action": "tokennfttx",
        "contract": contract,
        "address": address,
        "startblock": start,
        "endblock": end,
        "sort": "asc"
    }
    response = requests.get("https://api.polygonscan.com/api", params=parameters)
    return response.json()

# Get a list of 'ERC1155 - Token Transfer Events' by Address
def get_list_erc115_events_by_address(contract, address, start, end):
    parameters = {
        "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
        "module": "account",
        "action": "token1155tx",
        "contract": contract,
        "address": address,
        "startblock": start,
        "endblock": end,
        "sort": "asc"
    }
    response = requests.get("https://api.polygonscan.com/api", params=parameters)
    return response.json()

# Get list of Blocks Validated by Address
def get_list_blocks_by_address(address):
    parameters = {
        "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
        "module": "account",
        "action": "getminedblocks",
        "blocktype": "blocks",
        "address": address
    }
    response = requests.get("https://api.polygonscan.com/api", params=parameters)
    return response.json()

# Contracts
# Get Contract ABI for Verified Contract Source Codes
def get_contract_abi_verified_source_code(address):
    parameters = {
        "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
        "module": "contract",
        "action": "getabi",
        "address": address
    }
    response = requests.get("https://api.polygonscan.com/api", params=parameters)
    return response.json()

# Get Contract Source Code for Verified Contract Source Codes
def get_contract_source_code_verified_source_code(address):
    parameters = {
        "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
        "module": "contract",
        "action": "getsourcecode",
        "address": address
    }
    response = requests.get("https://api.polygonscan.com/api", params=parameters)
    return response.json()

# Get Contract Creator and Creation Tx Hash
def get_contract_creator_and_creation_hash(contracts):
    add_query = ""
    for i in contracts:
        add_query += i
    parameters = {
        "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
        "module": "contract",
        "action": "getcontractcreation",
        "contractaddresses": add_query
    }
    response = requests.get("https://api.polygonscan.com/api", params=parameters)
    return response.json()

# Transactions
# Check Transaction Receipt Status
def get_transaction_receipt_status(hash):
    parameters = {
        "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
        "module": "transaction",
        "action": "gettxreceiptstatus",
        "txhash": hash
    }
    response = requests.get("https://api.polygonscan.com/api", params=parameters)
    return response.json()

# Blocks
# Get Block Rewards by BlockNo
def get_block_rewards_by_blockno(block):
    parameters = {
        "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
        "module": "block",
        "action": "getblockreward",
        "blockno": block
    }
    response = requests.get("https://api.polygonscan.com/api", params=parameters)
    return response.json()

# Get Estimated Block Countdown Time by BlockNo
def get_estimated_block_countdown_time_by_blockno(block):
    parameters = {
        "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
        "module": "block",
        "action": "getblockcountdown",
        "blockno": block
    }
    response = requests.get("https://api.polygonscan.com/api", params=parameters)
    return response.json()

# - Get Block Number by Timestamp
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

# - Get Daily Average Block Size
def get_daily_average_block_size(start,end):
    parameters ={
    "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
    "module": "stats",
    "action": "dailyavgblocksize",
    "startdate": start,
    "enddate":end,
    "sort": "asc"
    }
    response = requests.get("https://api.polygonscan.com/api", params=parameters)
    return response.json()['result']

# - Get Daily Block Count and Rewards
def get_daily_block_count_and_rewards(start,end):
    parameters ={
    "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
    "module": "stats",
    "action": "dailyblkcount",
    "startdate": start,
    "enddate":end,
    "sort": "asc"
    }
    response = requests.get("https://api.polygonscan.com/api", params=parameters)
    return response.json()['result']

# - Get Daily Average Time for A Block to be Included in the Polygon POS Chain
def get_daily_avg_time_block_polygon_pos_chain(start,end):
    parameters ={
    "apikey": "G9JUJVPPH7N45HJGZNB69YM1Z93GM4RE83",
    "module": "stats",
    "action": "dailyblkcount",
    "startdate": start,
    "enddate":end,
    "sort": "asc"
    }
    response = requests.get("https://api.polygonscan.com/api", params=parameters)
    return response.json()['result']

