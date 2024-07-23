## Introduction to Logging
import logging

'''
DEBUG   -> Detalied info

INFO   -> Cofirmation that everything is working as expected

WARNING  -> The Code is working but there might be a potential problem in the future

ERROR     ->  Due to more serious problems , the functions cannot be performed

CRITICAl   -> The program may be unable to continue


'''
logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def divide(a,b):
    return a/b

def multiply(a,b):
    return a*b
a=6
b=3
add_result = add(a,b)
logging.warning('Add:{} + {} = {}'.format(a,b,add_result))

sub_result = subtract(a,b)
logging.warning(f"Sub : {a} - {b} = {sub_result}")

multiply_result = multiply(a,b)
logging.warning(f"Sub : {a} * {b} = {multiply_result}")

divide_result = divide(a,b)
logging.warning(f"Sub : {a} / {b} = {divide_result}")
