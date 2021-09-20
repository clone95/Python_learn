import os
from datetime import date


def ensure_dir(directory_name, add_date=False):
    
    if add_date == True:
        today = date.today()
        directory_name_with_date = directory_name + str(today)
        # a function that takes as input a directory name and checks is exists and if not it creates a new directory
        if not os.path.exists(directory_name_with_date):
            os.makedirs(directory_name_with_date)
    else:
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
        
