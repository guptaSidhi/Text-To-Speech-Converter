import os
import sys

def get_error_message_details(error_message,error_detail):
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    lineno = exc_tb.tb_lineno
    error = str(error_message)
    error_message = f"Error is occuring in [{filename}] at line number [{lineno}] with message [{error}]"
    return error_message

class CustomException(Exception):

    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = get_error_message_details(error_message,error_detail)
        

    def __str__(self):
        return self.error_message