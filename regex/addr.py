import re

name=input('enter your full name')
pattern="[a-zA-Z]+$"
if re.match(pattern,name):
    print('name valid')
else:
    print('name not valid')

contact=input('enter your number')
pattern2="^[0-9]{10}$"
if re.match(pattern2,str(contact)):
    print('contact valid')
else:
    print('contact invalid')

address=input('enter your address')
add="[a-zA-Z]+$"
if re.match(add,address):
    print('address valid')
else:
    print("invalid address")



# class,object,constructor,inheritance,scope,setter and getter