# success_attempt(sa)
# unsuccess attempt (usa)
name = "Akhil"
pwd = "1234"
usa = sa = 0

def dec(func):
    def wrapper(*args,**kwargs):
        print("Application started")
        func(*args,**kwargs)
    return wrapper

@dec
def login(username,password):
    global sa,usa
    if(username == name and password == pwd):
        sa += 1
        print("Login Successful")
    elif(username != name):
        usa += 1
        if(usa<=3):
            x = input("Enter username:")
            login(x,password)
        else:
            print("No more attempts")
    else:
        usa += 1
        if(usa<=3):
            x = input("Enter password:")
            login(username,x)
        else:
            print("No more attempts")
login(input(),input())
print("sa:",sa)
print("usa:",usa)