import os

# Function to write data into a file.
def wrt_data(data, path, filename="/summary_data"):
    f = open(path + filename, "a+")
    f.write(data + "\n")
    f.close()

# Function to make directory if not exists.
def make_dir(dirpath):
    os.makedirs(dirpath)

def write_accounts_data(accounts_data, path):
    with open(path, "a+") as f:
        for account in accounts_data:
            f.write("Name: " + str(account["booker_name"]) + "\n")
            f.write("Current Balance: " + str(account["current_balance"]) + "\n")
            f.write("Withdrawing Balance: " + str(account["pending_withdrawal"]) + "\n")
            f.write("--" + "\n")