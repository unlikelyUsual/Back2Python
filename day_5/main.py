# This module to under import/export modules

from functions import *
# from functions import add  # import single def

# TO import from folders, we import file as whole instead of functions like above
# from sub_module import fun1
# or all functions from the file
# from sub_module.fun1 import * 


print(add(10,300))

print(mul(10,2))

# print(fun1.some_functions())

# If we want to import the all function across multiple files in sub_module
# We have to make sub_module module as module(package) by creating __init__.py file
# from sub_module import *

from sub_module import * 
print(fun1.some_functions())
print(fun2.funtion2())

