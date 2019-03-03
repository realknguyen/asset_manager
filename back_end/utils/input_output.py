import os

# Function to write data into a file.
def wrt_data(data, path):
    f = open(path + "/summary_data", "a+")
    f.write(data + "\n")
    f.close()

# Function to make directory if not exists.
def make_dir(dirpath):
    os.makedirs(dirpath)

def write_accounts_data(accounts_data, path):
    for account in accounts_data:
        wrt_data("Name: " + str(account["booker_name"]), path)
        wrt_data("Current Balance: " + str(account["current_balance"]), path)
        wrt_data("Withdrawing Balance: " + str(account["pending_withdrawal"]), path)
        wrt_data("--", path)