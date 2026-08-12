# 1. write a python program to build a basic swiggy food ordering system using variables use the following types of data
# username, order_id, delivery_time, cart_items, available_restaurant, tax_bill
# initialize user details add multiple food items to the cart , add multiple restaurant, update order details, print final order summary
# use if in 10% discount

# solution
# initialize user details
username = "Akhil"
order_id = "9618abcd"
delivery_time = "30 mins"

# available restaurants
available_restaurant = {'mehfil','akshaya','abhiruchi'}

# cart items
cart_items = ['panner biryani','chicken biryani']

# adding cart items
# cart_items.extend(['cake','coke','icecream'])
cart_items += ['cake','coke','icecream']

# adding restaurants
# available_restaurant.add('paradise')
# available_restaurant.add('bawarchi')
available_restaurant |= {'paradise','bawarchi'}

# bill details
tax_bill = 67.00
bill_amount = 359

# update order details
delivery_time = "25 mins"

# total_bill
total_bill = bill_amount + tax_bill

# discount and final_bill
if(total_bill >= 300):
    discount = total_bill * 0.10
    final_bill = total_bill - discount
else:
    discount = 0
    final_bill = total_bill

# printing final order
print("********Swiggy order details:********")
print("username:",username) # string
print("order_id:",order_id) # string
print("delivery_time:",delivery_time) # string
print("available restaurants:",available_restaurant) # set
print("cart items:",cart_items) # list
print("tax bill:",tax_bill) # float
print("bill amount:",bill_amount)   #int
print("total bill:",total_bill) # float
print("discount:",discount) # float
print("final bill:",final_bill) # float



# discount= 10
# cart_value=300
# print(cart_value*(discount/100))

# 2. create a python program where a shopping cart contains a list of products and each product has list of features. Create a duplicate cart using shallow copy and modify the features of one product in the copied cart. check if the original cart changes then use the deepcopy and explain the difference

print("\n")
print("Shopping shallow copy and deep copy")
shopping_cart = [['shirt','pant'],['t-shirt','short'],['fruits','vegetables']]
print("Original shopping cart: ",shopping_cart)

# shallow copy
import copy
shal_cpy = copy.copy(shopping_cart)
print("shallow copy before modifications:",shal_cpy)
shal_cpy[1][0] = 'chocolate'
print('shallow copy after modifications: ',shal_cpy)
print('original shopping cart after shallow copy: ',shopping_cart)

# deep copy
deep_copy = copy.deepcopy(shopping_cart)
print("Deep copy before modifications:",deep_copy)
deep_copy[0][1] = 'linen-shirt'
print('deep copy after modification:',deep_copy)
print('original copy after modification by deep copy:',shopping_cart)

