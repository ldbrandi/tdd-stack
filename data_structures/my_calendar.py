'''This file will be used to test Mock() features.'''

import requests
from datetime import datetime


def is_weekday():
    '''This function returns True if it's a weekday, otherwise False.'''
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)

def get_holidays():
    '''Sample function to return a list of upcoming holidays'''
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None