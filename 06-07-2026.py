# 1. create a function calculate bill with parameters price & quantity that returns total cost, add 40/- delivery fee, if total is less than 200, call in one line and print result.

def calculate(price,quantity):
    total = price*quantity
    if(total<200):
        print("Additional delivery charges are added because bill amount is below 200rs")
        print("Adding 40rs small cart fee...")
        return total+40
    return total
price = int(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))
Total = calculate(price,quantity)
print("Total bill: ",Total)

print()

print("Total bill: ",calculate(int(input("Enter the price: ")),int(input("Enter the quantity: "))))


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

def total(subject1, subject2, subject3):
    return subject1+subject2+subject3

def avg(total):
    return total//3

def grade(avg):
    if avg>85:
        return "A"
    if avg>75:
        return "B"
    if avg>65:
        return "C"
    if avg>50:
        return "D"
    return "Fail"

Total = total(70,65,80)
Average = avg(Total)
Grade = grade(Average)
print("Grade:",Grade)

print()

print("Grade: ",grade(avg(total(int(input("Enter subject1 marks: ")),int(input("Enter subject2 marks: ")),int(input("Enter subject3 marks: "))))))

# 3. Create a python program to develop a simple ATM system where a user attempts to withdraw money or a deposit money your application should verify if sufficient balance is avaliable then display the remaining balance. Implement this using multiple functions like deposit, withdraw, check balance and produce the final output in a single statement.

def deposit(amount,current_balance):
    if amount>0:
        return amount+current_balance
    return "Enter a valid amount to deposit"

def withdraw(amount,current_balance):
    if amount > current_balance:
        return "pisal levv"
    return current_balance-amount

balance = int(input("Enter your balance:"))
balance = deposit(1000,balance)
print("Current balance: ",balance)
print(withdraw(2000,balance))

print(withdraw(10000,deposit(int(input("Enter your amount to deposit:")),int(input("Enter your balance: ")))))

