import json
from decimal import Decimal

# Read all bookmakers account data from bookmakers_data.json 
# Also include bank account balance 
def get_bookmakers_data():
    with open('./back_end/bookmakers/accounts_data/accounts_data.json') as json_data:
        accounts_data = json.load(json_data)
    return accounts_data

# Calculate the total account value
def get_bookmakers_total_value(accounts_data):
    total_value = 0
    for account in accounts_data:
        total_value += Decimal(account["current_balance"]) + Decimal(account["pending_withdrawal"])
    return total_value

# Calculate total number of bookmakers excluding bank account.
def get_total_number_of_bookmakers(accounts_data):
    return len(accounts_data) - 1

# List all the current bookmakers information
def get_bookmakers_information(accounts_data):
    for account in accounts_data:
        print("Name: " + str(account["booker_name"]))
        print("Current Balance: " + str(account["current_balance"]))
        print("Withdrawing Balance: " + str(account["pending_withdrawal"]))
        print("--")
        
# List all current bookmaker accounts summary
def get_all_bookmakers_summary(accounts_data):
    print("Total number of bookmakers: " + str(get_total_number_of_bookmakers(accounts_data)))
    get_bookmakers_information(accounts_data)
    print("Accounts total value: " + str(get_bookmakers_total_value(accounts_data)))
    sperate_str = "-------------------------------------------------"
    print(sperate_str)