from src.exception import CustomException
from src.logger import logging 
import sys

def get_accent_tld(user_input):

    try:
        accent_match = {
            'Australian': 'com.au',
            'South Africa': 'co.za',
            'British': 'co.uk',
            'Indian': 'co.in',
            'Canadian': 'ca',
            'Irish': 'ie',
            'Spanish': 'es'
        }

        ttld = accent_match[user_input]
        return ttld
    
    except Exception as e:
        raise CustomException(e,sys)
    
def get_accent_message():

    try:
        accent = ['Australian','South Africa','British','Indian','Canadian','Irish','Spanish']
        return accent
    
    except Exception as e:
        raise CustomException(e,sys)