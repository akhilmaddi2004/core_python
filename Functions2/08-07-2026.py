# arbitary parameters/ variable-length parameters
# variable no. of positional arguments or variable no. of keyword arguments
# variable length arguments

# Arbitary arguments in Python are parameters that allow a function to accept an unlimited or variable number of inputs when the exact count is unknown beforehand.
# They are categorized into two types:

# 1. Arbitary Positional Arguments(*args): 
# collects sequence data like list, tuple, set but stores tuple
# Denoted by an asterik(*), these collect multiple positional (non-keyword) arguments into a tuple.
# This allows functions to iterate over an unknown number of values, such as def add(*numbers):

# 1. arbitary positional arguments: (*args)
# *args to store multiple values, system stores args in tuple

def add(*args):
    print(args)
add(1,2,3,4,5,6,7,8,9)

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print("Total sum = ",add(1,2,3,4,5,67))

def add(*args):
    x = sum(args)
    return x
print(add(1,2,3,4,4))

# 2. arbitary keyword arguments(**kwargs):
# stores in dictionary
# Denoted by double asterisks(**), these collect multiple keyword arguments into a dictionary.
# This enables functions to handle named parameters dynamically, such as def print_info(**details):

# **kwargs - keyword arguments
# stores dictionary type of data

def order_details(**kwargs):
    print(kwargs)
order_details(order_id=1234,name = 'abcd',cart=['burger','chips','cola'],bill = 350,addons = True, sauce = 'abc sauce', veggies = ['Onions','Lemons'])

def order_details(**kwargs):
    for key,value  in kwargs.items():
        print(f"{key} : {value}")
order_details(order_id=1234,name = 'abcd',cart=['burger','chips','cola'],bill = 350,addons = True, sauce = 'abc sauce', veggies = ['Onions','Lemons'])

def add(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum 
print(add(1,2,3,4,5))

def print_info(**details):
    for key,value in details.items():
        print(f"{key}:{value}")
print_info(name = "Akhil", age = 22, Course = "python")

# 1. Write a function multiply_all(*args) that returns the product of all numbers passed.
# arbitary positional arguments
def multiply_all(*args):
    mul = 1
    for i in args:
        mul *= i
    return mul
print(multiply_all(2,3,434,22,7))

# 2. create a function display_tags(**kwargs)  that prints each keyword-value pair on its own line
def display_tags(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
display_tags(name = "AKhil", age = 22, city = "Hyderabad", course = "Python full stack")


# create a python application to develop a simple hospital billing system. Design functions like calculate_bill with positional arguments charges of variable/arbitary type and another function apply insurance with keyword arguments of arbitary type, and create a function add_taxes with keyword arguments of arbitary type. The program should accept multiple charges like consultation, tests, and treatement. Apply insurance reduction and then add tax.

def calculate_bill(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
c_bill = calculate_bill(10000,1000,2000,500,2000,5000)
print(c_bill)

def apply_insurance(**kwargs):
    for key,value in kwargs.items():
        print(F"{key} : {value}")
a_ins = apply_insurance(health_insurance = 10000, lic =2000)

def add_taxes(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
a_tax = add_taxes(consultation = 100, tests = 1000, treatment = 2000)

# c_bill = c_bill - a_ins    
# c_bill += a_tax
# print(c_bill)

