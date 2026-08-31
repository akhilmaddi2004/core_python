# Function
# Function is  block of code that is used to perform a set of actions
# Function are easier beacuse they provide reusability of code. They are easier to connect, debug & improve readability.

# syntax:
# def function_name(parameters): # function declaration 
    # body of function
    # return type # optional
# function_name(parameters/arguments) # function calling

def greet(name):
    print("Hi!",name)
greet("Nanna")

def say_hello():
    print("Welcome to Python!")
say_hello()

def add(a,b):
    print("Addition")
    print("a+b:",a+b)
add(10,20)

def sub(a,b):
    print("Subtraction")
    print("a-b:",a-b)
sub(20,10)

def mul(a,b):
    print("multiplication")
    print("a*b:",a*b)
mul(10,20)

def div(a,b):
    print("division")
    print("a/b",a/b)
div(20,10)

def area_of_rectangle(length,width):
    print("area of rectangle:",length*width)
area_of_rectangle(10,20)

def area_of_rectangle(length,width):
    return length*width
area_of_rectangle(10,20)

def area_of_rectangle(length,width):
    return length*width
print(area_of_rectangle(10,20))

def area_of_rectangle(length,width):
    return length*width
x = area_of_rectangle(10,20)
print("area of rectangle:",x)

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b 

x = add(10,20)
y = sub(20,30)
z = mul(x,y)
print(div(z,10))


