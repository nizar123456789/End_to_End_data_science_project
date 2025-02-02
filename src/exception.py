import sys 
from src.logger import logging 



def error_message_detail(error,error_detail:str):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename  
    error_message="An Error has occured in the file [{0}] in the line of [{1}] error message [{2}] ".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:str):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
        
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divided by zero error")
        raise CustomException(e,sys)
    