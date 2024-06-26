# .)Any excption which will ocur the sys will hve its information .
import sys 
from src.logger import logging
# .)error_detail:sys the errror detail will be present inside sys.
def error_message_details(error,error_detail:sys):
  
  # .)theexc_tb will contain line and file in which exception occured.
  _,_,exc_tb = error_detail.exc_info()
  
  # .)The blw will give the filename in which excption occured.
  file_name = exc_tb.tb_frame.f_code.co_filename
  
  error_message = "Error occured in python file script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
  return error_message
  
  

class CustomException(Exception):
  def __init__(self,error_message,error_detail:sys):
    super().__init__(error_message)
    self.error_message = error_message_details(error_message,error_detail=error_detail)
    
    def __str__(self):
      return self.error_message
    
    
# if __name__ == "__main__":
#   try:
#     a = 1/0
#   except Exception as e:
#     logging.info("Divide by zero")
#     raise CustomException(e,sys)
    