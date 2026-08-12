# memory management
x = 10
print("x:",x)
print("x id:",id(x))

x = 20
print("x:",x)
print("x id(after updating x with new variable):",id(x))

x += 10
print("x:",x)
print("x id(after adding 10 to the x):",id(x))

# after updating or modifying new object will create new reference/addresses

# byte
x =b"hi"
print(x)
x =b"hello"
print(x)

# shallow copy - if any changes are made in shallow copy  it will effect in original copy also

org_msgs=[['Hi','How are you?'],['wyd?','hello!']]
print('Original message: ',org_msgs)

# shallow copy
import copy
shal_cpy = copy.copy(org_msgs)
shal_cpy[1][0] = 'abhilash'
print("after shallow copy:",shal_cpy)
print("after shallowing org copy:",org_msgs)

# deepcopy - if any changes are occurred in deep copy it won't effect on original copy
org_msgs1=[['Hi','How are you?'],['wyd?','hello!']]
print('Original message: ',org_msgs1)

# deepcopy
dp_cpy = copy.deepcopy(org_msgs1)
dp_cpy[0][1] = "Akhil"
print("Deep copied msgs:",dp_cpy)
print("original msgs after deep copy: ",org_msgs1)

a = [[1,2,3],[4,5,6]]
import  copy
b= copy.deepcopy(a)
b[0][0] = 99
print('b:',b)
print('a:',a)

c = [[1,2,3],[4,5,6]]
d = copy.copy(c) 
d[0][0] = 99
print('d:',d)
print('c:',c)

# whatsapp
contacts = {'deepthi','hemanth','prabhas'} # contacts stores in set 
print("Contacts: ",contacts)
messages = ['hi','how are you?','Who?'] # messages can be modified so we have to store them in list
print("messages:",messages)
print("Id of messages",id(messages))
deepthi = {
    'username':'deepthi',
    'phone_no.':1234,
    'status':'busy'
}
print('deepthi profile:',deepthi)

print("Address of deepthi's status:",id(deepthi['status']))
deepthi['status'] = 'online'
print("Address of deepthi's status(after modifying the status):",id(deepthi['status']))


messages += ['busy?']
print(messages)
print(id(messages))