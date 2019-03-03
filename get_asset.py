# Main functions to list all current assets
# Giving a summary of each and save it to a storage accordingly
# Will automatically save data to a folder for progression/data analysis use.

# from back_end.bookmakers.bookmaker_value import *
import back_end.bookmakers.bkmaker_accs_valuations as bk_accs
import back_end.utils.date_time as date_utls
import back_end.utils.input_output as io_utls

# Record each account's value.
def update_current_account_values(dir_name, data):
    bk_accs.get_all_bookmakers_summary(data)
    io_utls.write_accounts_data(data, dir_name)

# Record accounts summary and total value.
def update_accs_summary(dir_name, data):
    noOfBookmakers = "Total number of bookmakers: " + str(bk_accs.get_total_number_of_bookmakers(data))
    accountValue = "Accounts total value: " + str(bk_accs.get_bookmakers_total_value(data))
    io_utls.wrt_data(noOfBookmakers, dir_name)
    io_utls.wrt_data(accountValue, dir_name)
    sperate_str = "-------------------------------------------------"
    io_utls.wrt_data(sperate_str, dir_name)

# Create data directory folder with name same as current time.
def create_required_dir():
    dir_name = "./account_summary_data/" + date_utls.get_current_foldername()
    io_utls.make_dir(dir_name)
    return dir_name

dir_name = create_required_dir()
accounts_data = bk_accs.get_bookmakers_data()
update_accs_summary(dir_name, accounts_data)
update_current_account_values(dir_name, accounts_data)