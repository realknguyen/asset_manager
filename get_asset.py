# Main functions to list all current assets
# Giving a summary of each and save it to a storage accordingly
# Will automatically save data to a folder for progression/data analysis use.
from back_end.bookmakers.bookmaker_value import *
import datetime

current_time = datetime.datetime.now()


accounts_data = get_bookmakers_data()
get_all_bookmakers_summary(accounts_data)