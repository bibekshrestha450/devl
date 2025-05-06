# for loop(collection)
# # while(true or false)
# students=['ram','hari',"sita",'gita']

# for name in students:
#     print(f"hello:{name}")

# numbers=[1,2,3,4,5,6,7,8,9,10]

# for even_number in numbers:
#     if even_number%2==0:
#        print(even_number)

# print(range(10))

# for i in range(10,0,-1):
     # print(i,end="")


# data=[12,13,6000,5000,600,4500,700,7000,5570,890]

# for num in data:
#      #    if 500<num<1000:
#           # print(num)
#      if num in range(500,1000):
#           print(num,end=" ")

# data=int(input("enter the number of element in list:"))
# students=[]

# for name in range(data):
#     name=input("enter your name:")
#     students.append(name)

# print(students)


# number=int(input('enter your number:'))


# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")

# i=10

# while i>=1:
#     print(i,end=" ")
#     i-=1

# data=['ram','sita','gita','hari']

# i=0
# while i<len(data):
#     print(data[i])
#     i+=1


# number=int(input("enter the number upto which you want table:"))
# i=0
# while i<=number:
#      for i in range(1,11):
#          print(f"{number} x {i} = {number * i}")






# data=['ram','sita','gita','hari','ram','hari']
# new_data=[]
# for name in data:
#      if name not in new_data:
#           new_data.append(name)

# print(new_data)


# numbers=[
#     [12,14,15,16,89],
#     [98,87,65,43,21]
# ]
# new_data=[]
# for number in numbers:


#     new_data.extend(number)
# print(new_data)

# students = [
#     {'name': 'ram', 'address': 'ktm'},
#     {'name': 'sita', 'address': 'ktm'},
#     {'name': 'hari', 'address': 'ktm'},
#     {'name': 'gita', 'address': 'ktm'}
# ]

# for student in students:
#     print(f"My name is {student['name']} and I live in {student['address']}")


# number=int(input('enter the number'))

# if number >1:
#     i = 1
#     while i <= number:
#         print(f"Multiplication Table for {i}:")
#         j = 1
#         while j <= 10:
#             print(f"{i} x {j} = {i * j}")
#             j += 1
#         i += 1
# else:
#     print("Please enter a number greater than 1."



# students=[
#     {'name':'ram','makrs':[67,87,56,76,90]},
#     {'name':'sita','makrs':[97,90,56,76,90]},
#     {'name':'gita','makrs':[34,87,52,12,87]},
#     {'name':'hari','makrs':[67,13,56,15,45]}
# ]

# for student in students:
#     total=0
#     for mark in student['makrs']:
#         total+=mark
#         per=total/5
#         grade=''

#     if per>80:
#         grade="A"

#     elif per>60:
#          grade="B"

#     elif per>40:
#         grade="C"

#     elif per>33:
#         grade='D'

#     else:
#         grade='fail'

#     print(f"students name:{student['name']},total:{total},percentage:{per},grade:{grade}")
# total=0
# for x in range(1,51):
#     if x%2==0:
        # total+=1

# print(total)



# total users
# total male
# total female
# total active users
# total inactive users
# total active male
# total active female
# total inactive male
# total inactive female


# students = [
#     {'name': 'ram', 'gender': 'male', 'status': True},
#     {'name': 'sophia', 'gender': 'female', 'status': False},
#     {'name': 'gopal', 'gender': 'male', 'status': False},
#     {'name': 'hari', 'gender': 'male', 'status': False},
#     {'name': 'sita', 'gender': 'female', 'status': True}
# ]


# total_users = 0
# total_male = 0
# total_female = 0
# total_active = 0
# total_inactive = 0
# total_active_male = 0
# total_active_female = 0
# total_inactive_male = 0
# total_inactive_female = 0

# for student in students:
#     total_users += 1

#     if student['gender'] == 'male':
#         total_male += 1
#         if student['status']:
#             total_active_male += 1
#         else:
#             total_inactive_male += 1
#     elif student['gender'] == 'female':
#         total_female += 1
#         if student['status']:
#             total_active_female += 1
#         else:
#             total_inactive_female += 1

#     if student['status']:
#         total_active += 1
#     else:
#         total_inactive += 1


# print("Total users:", total_users)
# print("Total male:", total_male)
# print("Total female:", total_female)
# print("Total active users:", total_active)
# print("Total inactive users:", total_inactive)
# print("Total active male:", total_active_male)
# print("Toall active female:", total_active_female)
# print("Total inactive male:", total_inactive_male)
# print("Total inactive female:", total_inactive_female)




category=[
    {'cid':1,'name':'laptop'},
    {'cid':2,'name':'mobile'},
    {'cid':3,'name':'tv'},
]


products=[
    {'pid':1,'cid':1,'name':'dell','price':50000,'qty':10},
    {'pid':2,'cid':1,'name':'mac','price':90000,'qty':8},
    {'pid':3,'cid':2,'name':'mi','price':20000,'qty':60},
    {'pid':4,'cid':3,'name':'sony','price':15000,'qty':30},

]
products_name=0
quantity=0
price=0

for i in category:
    category_name = i['name']
    print(f"Category: {category_name}")
    
    for p in products:
        if p['cid'] == i['cid']:
            product_name = p['name']
            price = p['price']
            quantity = p['qty']
            print(f"  - Product: {product_name}, Price: {price}, Quantity: {quantity}")


# for i in range(1,6):
#     for r in range(1,i+1):
#         print(r,end=" ")
#     print()


# for i in range(5,0,-1):
#     for r in range(1,i+1):
#         print(r,end="")
#     print()

# for i in range(1,6):
#     print('*'*i)


# for i in range(5,0,-1):
#     print('*'*i)



# number=[]
# rep=[]

# n = int(input('How many numbers do you want to enter? '))

# for i in range(n):
#     num=int(input('enter the number:'))
#     number.append(num)

# for num in number:
#     if number.count(num)>1 and num not in rep:
#         rep.append(num)


# print(rep)




