# Main functions to list all current assets
# Giving a summary of each and save it to a storage accordingly
# Will automatically save data to a folder for progression/data analysis use.

# from back_end.bookmakers.bookmaker_value import *
import back_end.bookmakers.bkmaker_accs_valuations as bk_accs
import back_end.utils.date_time as date_utls

accounts_data = bk_accs.get_bookmakers_data()
bk_accs.get_all_bookmakers_summary(accounts_data)

date_utls.print_current_date()