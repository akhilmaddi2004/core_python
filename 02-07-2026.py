# Functions
# Function is a block of code, and resuable 
# we define function with 'def' keyword
# the information passsed to the functions is called parameters/arguments
# a function without parameters is called non-parameterized function

# in functions we have types
# 1. Function without parameters and without return type
# 2. Function without parameters and with return type
# 3. Function with parameters and without return type
# 4. Function with parameters and with return type

# 1. Function without parameters and without return type
def m1():
    print("Hi Class!")
    # automatically returns none if we print calling funtion like this print(m1())
m1()

def m1():
    print("Hi Class!")
m1()
print(m1()) # returns none after execution if we don't have return type in function code block

# 2. without parameters and with return type
def m1():
    return "Hi! Class"
m1() # prints nothing

def m1():
    return "Hi! Class"
m1() # prints nothing
print(m1())

# 3. with parameters and without return type
def m1(x):
    print(x)
m1(10)

def learn(name,skill):
    print('Hi!,',name,"is learning",skill)
    print("Hi!, "+name+" is learning "+skill)
learn("Akhil","Python")

# 4. with parameter and with return type
def add(a,b):
    return a+b
add(10,20) # returns nothing
print(add(10,20))

def remainder(a,b):
    print(a%b)
remainder(10,2)
remainder(9,2)

def rem(a):
    print(a%2)
rem(10)

# 1. Write a function called say_hello() that prints "Welcome to Python!"
def say_hello():
    print("Welcome to Python!")
say_hello()

# 2. Write a function called add(a,b) that returns the sum two numbers
def add(a,b):
    return a+b
print(add(234873,2387932))

# 3. What is the output of a function that has not return statement? Write a function to verify this.
def name(name):
    print(name)
name("Akhil")
print(name("Hello"))

# 4. Write a function area_of_rectangle(length,width) that returns length*width. call it with values 6 and 4
def area_of_rectangle(length,width):
    print("area:",length*width)
    return length*width
print(area_of_rectangle(6,4))

# 5. Explain in your own words: why do we use functions instead of writing code directly?
# - to reduce code lines and to reuse the code repeated where it's required
# - improves readability
print("to reduce code lines and to reuse the code repeated where it's required")