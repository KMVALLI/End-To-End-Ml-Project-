# writting own coustome exception 
# if any exception will get rasid the sis liberary  contain that information automatically

import sys 
import logging

def error_message_details(error,error_details:sys): # first parameter as a error what ever we got and second parameter error details it that error contain in sys module 
    _,_,exc_tb = error_details.exc_info() # exe_info() wil give three  out put we want to last out put we storeded as a exc_tb it contain error deatais completely information
    file_name = exc_tb.tb_frame.f_code.co_filename   #  hear we will get the  error file name what file we got a error 
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error)) #  3 rd place holder error we will get error message what ever we have got from  error_message_details() funcrion 

class CoustomException(Exception):
    def __init__(self,error_message,error_details:sys): 
        super().__init__(error_message) # inherting from base exception so we called super and also over ridden the  init method 
        self.error_message =error_message_details(error_message,error_details=error_details) 
    

    def __str__(self): #what ever the object you passed that will convert in the form of string 
        return self.error_message
    





    # where ever we you try excet we will rased the coustomException this type of message we will get  this  we will use every whwew in one time 