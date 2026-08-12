# create a python application to develop a simple hospital billing system. Design functions like calculate_bill with positional arguments charges of variable/arbitary type and another function apply insurance with keyword arguments of arbitary type, and create a function add_taxes with keyword arguments of arbitary type. The program should accept multiple charges like consultation, tests, and treatement. Apply insurance reduction and then add tax.

def calculate_bill(*bill):
    total_bill = 0
    for i in bill:
        total_bill += i
    return total_bill

def apply_insurance(amount,**insurance):
    total_claim = 0
    for key, value in insurance.items():
        print(f"{key} : {value}")
        total_claim += value
    return amount - total_claim

def calculate_taxes(amount, **taxes):
    total_taxes = 0
    for key,value in taxes.items():
        print(f"{key} : {value}")
        total_taxes += value
    return amount + total_taxes

total_bill = calculate_bill(1000,2000,20000)
total_bill = apply_insurance(total_bill, LIC = 1000, star = 4500)
print("Total bill: ",calculate_taxes(total_bill, SGST = 100, CGST = 200))


def add(*l):
    print(l)
    print(type(l))
add(1,2,3,4,5)

def add(*l):
    sum = 0
    for i in l:
        sum += i
    return sum
print(add(1,2,3,434,3,2,445))

def emp_details(**kwargs):
    print(kwargs)
    print(type(kwargs))
emp_details(emp_name = "Akhil", emp_id = 2210, emp_salary = 10000)
emp_details(emp_id = 20302, emp_salary = 10000, emp_name = "Akhil", emp_designation = "HR", emp_department = "HR & RD")

def emp_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
emp_details(emp_name = "Akhil", emp_id = 2210, emp_salary = 10000)
emp_details(emp_id = 20302, emp_salary = 10000, emp_name = "Akhil", emp_designation = "HR", emp_department = "HR & RD")

