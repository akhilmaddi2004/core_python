def learn(name,skill):
    print(name,"is learning",skill)
learn("sql","raju")
learn("raju","sql")
learn(skill="sql",name="Akhil")

# keyword arguments - improves readability, to assign correct arguments when we pass arguments in function
# by using positional arguments we give directly we won't specify

def objective(name,strength1,strength2,strength3):
    print("My name is ",name)
    print("My strength1 is ",strength1)
    print("My strength2 is ",strength2) 
    print("My strength3 is ",strength3)
objective(strength2="Analytical thinking",strength3="Collaborative",strength1="Problem solving",name="Akhil")

# Write a python program to bulit a simple uber application that has a function called trip_details with parameters like driver_name, pickup_location, drop_location, total_price
# now call this function using  positional arguments and keyword arguments
def trip_details(driver_name,pickup_location,drop_location,total_price):
    print("Your driver name is ",driver_name,"\nYour pickup_location is ",pickup_location,"\nYour drop_location is ",drop_location,"\nYour total_bill is ",total_price)
trip_details("Raju","JBS","KPHB",98)
print()
trip_details(drop_location="KPHB",pickup_location="JBS",driver_name="Raju",total_price=98)

# positional arguments
# 1. Write a function intro(name,city,hobby) that prints a sentence about a person. Call it in two different orders and observe the difference.
def intro(name,city,hobby):
    print("My name is ",name,",iam living in",city,"and my hobby is ",hobby)
intro("Akhil","Hyderabad","Coding")
intro("Coding","Hyderabad","Akhil")

# 2. Create subtract(a,b) that returns a-b. What is the difference between subtract(10,3) and subtract(3,10)
def sub(a,b):
    return a-b
print(sub(10,3))
print(sub(3,10))
print(sub(b=3,a=10))

# 3. What does 'positional' mean in 'positional arguments'? Write it in your own words.
#  The positional in 'positional arguments' is the position of arguments/parameters to pass arguments in functions

# 4. Write a function bio(first_name,last_name,age) and call it correctly using positional arguments.
def bio(first_name,last_name,age):
    print("First_name ",first_name,"Last_name ",last_name,"Age ",age)  
bio("Maddi","Akhil",22)

# 5. Can you pass more positional arguments than there are parameters? What error do you get?
def bio(first_name,last_name,age):
    print("First_name ",first_name,"Last_name ",last_name,"Age ",age)  
bio("Maddi","Akhil",22)

# TypeError: bio() takes 3 positional arguments but 4 were given

# keyword arguments

# 1. Call the function send_email(to,subject,body) using keyword arguments in any order.
def send_email(to,subject,body):
    print("Email: ",to)
    print("Subject of email: ",subject)
    print("Body of the email: ",body)
send_email(subject="Applying for leave",body="My health condition is very poor\ncan i get the leave for two days",to="akhilmaddi@gmail.com")


# 2. Write a function create_profile(username, email, age) and call it using keyword arguments.
def create_profile(username,email,age):
    print("My username is ",username)
    print("My email:",email)
    print("I am",age,"years old")
create_profile(age=22,email="akhilmaddi@gmail.com",username="Akhil")

# 3. What is the error if you place a positional argument after a keyword argument? Test it.
def create_profile(username,email):
    print("My username is ",username)
    print("My email:",email)
    # print("I am",age,"years old")
# create_profile(age=22,"akhilmaddi@gmail.com",username="Akhil")
# SyntaxError: positional argument follows keyword argument

# create_profile("akhilmaddi@gmail.com",username="Akhil")
# TypeError: create_profile() got multiple values for argument 'username'

create_profile("akhilmaddi@gmail.com",email="Akhil")
# SyntaxError: positional argument follows keyword argument

# 4. Rewrite this call using keyword arguments: book_ticket("Alice","Delhi","Mumbai",2)
def book_ticket(name,pickup_station,drop_station,tickets):
    print("My name is",name,"I am going to travel from",pickup_station,"to",drop_station,"with my friends and we took",tickets,"tickets.")
book_ticket(name="Alice",drop_station="Mumbai",pickup_station="Delhi",tickets=2)

# 5. Why are keyword arguments considered more readable? Write an example that demonstrates this clearly.
# Keyword arguments used everytime because of interchanging of the arguments when passed to functions so we can call them in any order by using keyword arguments then by using them we can improve the readability


