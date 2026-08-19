# success_attempt(sa)
# unsuccess attempt (usa)
sa = usa = 0
username = "Akhil"
password = "1234"

def dec(func):
    def wrap(*args,**kwargs):
        print("Application Started")
        func(*args,**kwargs)
    return wrap

@dec
def login(username1,password1):
    if(username1 == username and password1 == password):
        global sa
        sa += 1
        print("Login success")
    else:
        global usa
        usa += 1
        if(usa>=3):
            print("3 attempts are completed login after 24hrs")
        else:
            print("Try again")
login(input(),input())
login(input(),input())
login(input(),input())
# login(input(),input())
print(usa)
print(sa)
