import sys
# from logger import get_log_object
# log = get_log_object()

def error_message_details(error, error_detail:sys):
    """
    this function is to log error details.
    Params:
        error : name of error
        error_details : description about error
    """
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error Occured in python script name [{0}] at line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):

    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message

