# Repo for converting date and time formats

import datetime
from datetime import datetime

# Function to convert date format
def convert_date(submitted_date):

    create_date_list= submitted_date.split("-")
    date_list = list(map(int, create_date_list))

    return date_list
