import datetime

def get_current_date():
    return datetime.datetime.now()

def print_current_date():
    print(datetime.datetime.now())

# Function to return current time in ISO format for folder name.
def get_current_foldername():
    d = get_current_date()
    time_string = d.isoformat()
    result = time_string.replace(":", "-")
    return result