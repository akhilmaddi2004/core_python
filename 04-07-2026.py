# 1. Write a function multiply(a,b,c) that returns the product of three numbers.

def multiply(a,b,c):
    return a*b*c 
mul = multiply(10,20,12)
print("multiply of three numbers:",mul)

# 2. Create a function describe_pet(animal,name) that prints: 'My [animal] is named [name].'

def describe_pet(animal,name):
    print("My",animal,"is named",name)
    print("My "+animal+" is named "+name)
describe_pet("Dog","Chintu")

# ,  in concatenating when we use ,(comma) for spacing it gives default spaces
# but we use (+) then we have create manually spaces where required
 
# 3. What happens if you call a function with fewer arguments than parameters? Try it and note the error.

def describe_pet(animal,name):
    print("My",animal,"is named",name)
    print("My "+animal+" is named "+name)
# describe_pet("Dog")
# TypeError: describe_pet() missing 1 required positional argument: 'name'

# 4. Write a function power(base,exponent) that returns base raised to exponent using the ** operator
def power(base,exponent):
    return base ** exponent
print("Power(9,3):",power(9,3))

# 5. create a function full_name(first,middle,last) returns the full name as a single string
def full_name(first,middle,last):
    return first,middle,last
print(full_name("Shyam","Singa","Roy"))

def full_name(first,middle,last):
    return first+' '+middle+' '+last
print(full_name("Shyam","Singa","Roy"))

# calling more than 2 functions in a single line
def add(a,b):
    return a+b 

def sub(a,b):
    return a-b 

def mul(a,b):
    return a*b 

def div(a,b):
    return a/b 

x = add(10,20)
y = sub(30,20)
z = mul(x,y)
print("div:",div(z,10))

print(div(mul(add(10,20),sub(30,20)),10))

# 1. create a function calculate bill with parameters price & quantity that returns total cost, add 40/- delivery fee, if total is less than 200, call in one line and print result.
def calculate(price,quantity):
    total = price * quantity
    if(total<200):
        total+=40
    return total
print(calculate(40,3))

def calculate1(price,quantity):
    return price*quantity
total = calculate1(40,3)
if(total<200):
    total+=40
print(total)

# 2. create a python application with three functions 
# first fun_name with total with three parameters of 3 subjects marks
# next fun_name avg of total marks in three subjects
# create another function with grade that takes avg as input, 
# if avg is 85% > return "A" grade
# if avg is 75% to 85%  return "B" grade
# if avg is 65% to 75% return "C" grade
# if avg is 50% to 65% return "D" grade
# else return fail
# call it in a single line 

def total(sub1,sub2,sub3):
    return sub1+sub2+sub3
T = total(87,67,45)
print("Total marks:",T)

def average(T):
    return T/3
A = average(T)
print("Average:",A)

def grade(A):
    if(A>=85):
        return "Grade A"
    elif(A>=75 and A<=85):
        return "Grade B"
    elif(A>=65 and A<=75):
        return "Grade C"
    elif(A>=50 and A<=65):
        return "Grade D"
    else:
        return "Fail"
print(grade(A))
print(grade(average(total(87,67,45))))

print(grade(average(total(75,75,75))))

# 3. Create a python program to develop a simple ATM system where a user attempts to withdraw money or a deposit money your application should verify if sufficient balance is avaliable then display the remaining balance. Implement this using multiple functions like deposit, withdraw, check balance and produce the final output in a single statement.

def ATM(check_balance,deposit,withdraw):
    check_balance = 2000
    deposit += check_balance 
    print(deposit)
    if(check_balance>= withdraw):
        print("Withdraw Your money")
    else:
        print("Insufficient Balance")
    check_balance -= withdraw
    print(withdraw)
    return check_balance
print(ATM(2000,5,100))

def check_balance(balance):
    return balance
Bal=check_balance(2000)
print("Balance:",Bal)

def deposit(add_amount,Bal):
    if (Bal<0):
        print("Minus Bank Balance")
    else:
        print("Add Your Amount")
    Bal += add_amount
    return Bal
print(deposit(500,Bal))

def withdraw(withdraw_amt,Bal):
    if(Bal>=withdraw_amt):
        print("Withdraw your amount")
    else:
        print("Insufficient Balance")
    Bal -= withdraw_amt
    return Bal
print(withdraw(1000,Bal))

