def trip_details(driver_name,pickup_location,drop_location,fare):
    print("Your driver's name:",driver_name)
    print("From:",pickup_location)
    print("To:",drop_location)
    print("Fare:",fare)

trip_details("Subbu","KPHB","JBS",120)
trip_details(120,"Subbu","JBS","KPHB")

trip_details(pickup_location="JBS",drop_location="KPHB",fare=120,driver_name="Raju")

# positional arguments must be before the keyword arguments because order matters in positional arguments
trip_details("Subbu","KPHB",fare=120,drop_location="Hitech-city")

# trip_details(driver_name="Subbu","KPHB",fare=120,drop_location="Hitech-city")
# SyntaxError: positional argument follows keyword argument

# ### default parameters: if we won't pass the arguments then default parameters will get pass through the arguments in functions

def greet(username):
    print("Hello!",username)
greet("Akhil")

# greet() TypeError: greet() missing 1 required positional argument: 'username'
# so we use default parameters in functions

def greet(username= "user"):
    print("Hello!",username)
greet()
greet("Arjun")
# if we pass the new value in arguments we get new updated value if not it gives output as default values

# place default value at last in decalration of the function if not we get error
# def greet(name="User",age):

def greet(age,name="User"):
    print("Hello!",name)
    if(age>18):
        print("Your are eligible to vote")
    else:
        print("Your are not eligible for vote")
greet(20)
greet(17)
greet(19,"Akhil")

# 1. Write a function power(base, exponent=2) that returns base^exponent. Test with one and two arguments.

def power(base,exponent=2):
    print("power")
    return base**exponent
print(power(20))
print(power(base=22,exponent=3))
print(power(base=4))
# print(power(exponent=4)) 
print(power(exponent=3,base=4))
print(power(6,3))
print(power(3,1))

# 2. create a function connect(host,port=3306,protocol="TCP") and call it various combinations
def connect(host,port=3306,protocol="TCP"):
    print("Connect to host:",host)
    print("Port:",port)
    print("Protocol:",protocol)

connect("localhost")
connect("localhost1",3308,"TCP")
connect("localhost2",3309,"UDP")
connect("localhost3:127.0.0.1",port=3309,protocol="TCP")
connect(port=3309,protocol="UDP",host="locals")

# connect(port= 33,protocol="UDP")
connect(host="LOcal",port=33)

# 3. What is the syntaxError in: def func(name="Guest",age)? Fix it.
# def func(name="Guest",age):
# # SyntaxError: parameter without a default follows parameter with a default

def func(age,name="Guest"):
    print("Hello!",name)
    print("Age:",age)
func(20)
func(age=21,name="Akhil")
func(20,"akhil")

# 4. Write a function discount_price(price,discount=10) that returns the discounted price.
# Test with and without the discount argument
def discount_price(price,discount=10):
    discounted_price = price - discount
    return discounted_price
print(discount_price(200))
print(discount_price(200,20))
print(discount_price(price=200,discount=20))
print(discount_price(price=100))


# 5. Why would you use a default parameter instead of just hardcoding a value inside the function? Explain with an example.

def greet(name,age):
    print("Hello",name)
    if age>=18:
        print("You are eligible to vote")
    else:
        print("you are not eligible to vote")

def greet(age,name="User"):
    print("Hello",name)
    if age>=18:
        print("You are eligible to vote")
    else:
        print("you are not eligible to vote")
greet(20)

greet(17)

greet(22,"Akhil")
greet(age=21)
greet(age=23,name="Akhil")

