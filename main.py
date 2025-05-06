# nep =int(input("Enter Nepali marks: "))
# eng =int(input("Enter English marks: "))
# math =int(input("Enter Math marks: "))
# phy =int(input("Enter Physics marks: "))
# chem =int(input("Enter Chemistry marks: "))
# total = nep+eng+math+phy+chem
# per = total/5
# print("Total marks: ", total)
# print("Percentage: ", per)
# if per>80:

#     print("A+")
# elif per>60:
#     print("A")
# elif per>40:
#     print("B")

# else:
#     print("C")


# products = {
#     1: {"name": "Dell", "price": 20000},
#     2: {"name": "HP", "price": 30000},
#     3: {"name": "Lenovo", "price": 40000},
#     4: {"name": "Apple", "price": 50000}
# }
# print(input("inter your name:"))
# choice = int(input("Enter your choice: "))
# quantity = int(input("Enter your quantity: "))

# name=products[choice]["name"]
# price=products[choice]['price']
# total=price*quantity

# name=input("enter your name:")

# if name=="admin":
#     age=input("enter your age")
#     print(name)
#     print(age)

# else:
#     print("enter your name")
    
# username=input("enter your username:")
# password=input("enter your password")

# if username=="admin":
#     if password=="aadmin234":
#         print("welcome to the system")
#     else:
#          print("envalid password")
# else:
#     print("envalid username")

# print("welcome")
# pin=int(input("enter your pin"))
# if pin==123:
#     pass
#     amount=10000
#     print("1.balance enquary 2.withdraw")
#     optinon=int(input('your option:'))
#     if optinon==1:
#         print("your balance is",amount)
#     elif optinon==2:
#         withdraw=int(input("amount you want to withdraw:"))
#         if withdraw<=amount:
#             print("please collect amoumt you want to withdraw")
#             print("your withdraw amount is",withdraw)
#             amt=amount-withdraw
#             print("your remaining balance is",amt)
#         else:
#             print("ensuficient balance")
#     else:
#         print("invalid option")
# else:
#     print("invalid pin")

# username=input('enter your username:')
# password=input('enter your password:')
# if username=="admin":
#     if password==1234:
#         print('welcome')
#         age=("enter your age:")
# #         if age<=18:
# # #             print('you can only drink soft drink')
# # #         elif age<=40:
# # #                 print("you can only drink soft drink and wine")
# # #         else:
# # #             print("you can drink any drink you want")
# # #     else:
# # #          print("Invalid password please try again.")
# # # else:
# # #      print("Invalid username please try again")


# # a=int(input('enter your first nummber:'))
# # b=int(input('enter your second number:'))
# # c=int(input('enter your third number:'))
# # if a>b and b>c:
# #      print(a,b,c)
# # elif b>a and a>c:
# #      print(b,a,c)
# # elif c>a and a>b:
# #      print(c,a,b)   
# # elif b>c and c>a:
# #      print(b,a,c)
# # elif b>c and c>a:
# #      print(b,c,a)
# # else:
# #      print(c,b,a)

# a=int(input('enter your first nummber:'))
# b=int(input('enter your second number:'))
# c=int(input('enter your third number:'))
# if a>b and b>c:
#      print(a,b,c)
# elif b>a and a>c:
#      print(b,a,c)
# elif c>a and a>b:
#      print(c,a,b)   
# elif b>c and c>a:
#      print(b,a,c)
# elif b>c and c>a:
#      print(b,c,a)
# else:
#      print(c,b,a)               
           
# # #choice
# # #delevery
# # #home1000 pick free
# # #pack palastic box
# # #location

# # print("Choose a laptop:")
# # print("1. Dell (Rs: 20000)")
# # print("2. HP (Rs: 30000)")
# # print("3. Lenovo (Rs: 40000)")
# # print("4. Apple (Rs: 50000)")

# # choice = input("Enter your choice (1-4): ")

# # if choice == '1':
# #     name='dell'
# #     quantity=int(input())
# #     price=20000
# # elif choice == '2':
# #     name="hp"
# #     price=30000
# # elif choice == '3':
# #     name="lenove"
# #     price=40000
# # elif choice == '4':
# #     name="apple"
# #     price=50000
# # else:
# #     print("invalid choice")


# # print("the name of laptop is",name,"and the price is",price)


# # print("delevery option are given below:")
# # print('1.home delevery(rs1000)')
# # print("2.pickup(free)")
# # delevery=input("enter your choice (1 or 2):")

# # if delevery==1:
# #     delevery_price=1000
    



# # print("which will you prefeer")
# # print("1.palastic wraped")
# # print("2.box")
# # packed=input("enter you choice(1 or 2)")
# # if packed==1:
# #     print("the laptop will be wraped in palastic")
# # elif packed==2:
# #     print("tthe laptop will be brought in box ")


# # customer=input("customer name:")
# # address=input('customer address')

# # print(customer)
# # print(address)


# # print("*************bill**************")


# # print('********thanks for visiting***********')


# print("*********************new road travels*******************")
# print("total km=27km")
# print('total stop=6')
# print("the place you wana travell choose from below:")

# # option for stops
# print("1.manamaiju-nepaltar")
# print("2.manamaiju-machapokhari")
# print('3.manamaiju-kalanki')
# print("4.manamaiju-kirtipur")
# print("5.manamaiju-putali sadak")
# print("6.manamiju-new road")

# #customers choice
# stop=int(input("enter your stop from (1-6)"))

# if stop==1:
#     price=15
# elif stop==2:
#     price=30
# elif stop==3:
#     price=45
# elif stop==4:
#     price=60
# elif stop==5:
#     price=75
# elif stop==6:
#     price=85
# else:
#     print("Invalid stop")


# #discount for student
# print("do you have student id card?")
# student_id=input("1.yes or 2.no:")
# if student_id==1:
#     discount=0.4
# elif student_id==2:
#     pass
# else:
#     print('invalid choice')
# print("***************************travelling bill ********************** ")
# #traveller name and bill
# name=input("entter your name :")

# print("traveller name:",name)

# discount=price*40/100
# total=price-discount
# print(total)

# print("your total travelling bill is ",total)

# print('**********************come again*******************************')


a=int(input('enter your first nummber:'))
b=int(input('enter your second number:'))
c=int(input('enter your third number:'))
if a>b and b>c:
     print(a,b,c) and print(c,b,a)
elif b>a and a>c:
     print(b,a,c) and print(c,a,b)
elif c>a and a>b:
     print(c,a,b) and print(b,a,c)
elif b>c and c>a:
     print(b,a,c) and print(c,a,b)
elif b>c and c>a:
     print(b,c,a) and print(a,c,b)
else:
     print(c,b,a) and print(a,b,c)          

if a>b and b>c:
      print(c,b,a)
elif b>a and a>c:
     print(c,a,b)
elif c>a and a>b:
     print(b,a,c)
elif b>c and c>a:
     print(c,a,b)
elif b>c and c>a:
     print(a,c,b)
else:
     print(a,b,c)          


     