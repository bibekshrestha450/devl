# exe 1
# for i in range(1,11):
#     print(i)
# exe 2
# sum=0
# for i in range(1,11):
#     sum+=i

# print(sum)


# num=int(input("enter the number"))
# i=0
# while i<=num:
#     for i in range(1,11):
#        print(f'{num}X{i}={num*i}')
    
    
# number=int(input("enter the number upto which you want table:"))
# if number>1:
#     i=1
#     while i <=number:
#         print(f"the table of {i}")
#         j=1
#         while j<=10:
#             print(f'{i}X{j}={i*j}')
#             j+=1
#         i+=1
     # number=int(input('enter the number'))

# if number >1:
#     i = 1
#     while i <= number:
#         print(f"Multiplication Table for {i}:")
#         j = 1
#         while j <= 10:
# #             print(f"{i} x {j} = {i * j}")
# #             j += 1
# #         i += 1

# # count=0
# # for i in range(1,10):
# #     if i%2==0:
# #         count+=1
# #         print(i)
# # print(count)


students=[
    {'name':'ram','gender':'male','status':True},
    {'name':'sophia','gender':'female','status':False},
    {'name':'gopal','gender':'male','status':False},
    {'name':'hari','gender':'male','status':False},
    {'name':'sita','gender':'female','status':True},

]


users = 0
male = 0
female = 0
active = 0
inactive = 0
active_male = 0
active_female = 0
inactive_male = 0
inactive_female = 0

for student in students:
    users+=1
    if student['gender']=="male":
        male+=1
        if student["status"]==True:
            active_male+=1
        else:
            inactive_male+=1
    else:
        female+=1
        if student["status"]==True:
            active_female+=1
        else:
            inactive_female+=1

    if student["status"]==True:
        active+=1
    else:
        inactive+=1

print(f'total user:{users}')
print(f'total male:{male}')
print(f'total female:{female}')
print(f'total active user:{active}')
print(f'total active male:{active_male}')
print(f'total active female:{active_female}')
print(f'total inactive male:{inactive_male}')
print(f'total inactive female:{inactive_female}')


# students=[
#     {'name':'ram','gender':'male','status':True},
#     {'name':'sophia','gender':'female','status':False},
#     {'name':'gopal','gender':'male','status':False},
#     {'name':'hari','gender':'male','status':False},
#     {'name':'sita','gender':'female','status':True},

# ]


# users = 0
# male = 0
# female = 0
# active = 0
# inactive = 0
# active_male = 0
# active_female = 0
# inactive_male = 0
# inactive_female = 0

# for student in students:
#     users+=1
#     if student["gender"]=="male":
#         male+=1
#         if student["status"]==True:
#             active_male+=1
#         else:
#             inactive_male+=1
#     else:
#         female+=1
#         if student["status"]==True:
#             active_female+=1
#         else:
#             inactive_female+=1

#     if student["status"]==True:
#         active+=1
#     else:
#         inactive+=1

# print(f'total user:{users}')
# print(f'total male:{male}')
# print(f'total female:{female}')
# print(f'total active user:{active}')
# print(f'total active male:{active_male}')
# print(f'total active female:{active_female}')
# print(f'total inactive male:{inactive_male}')
# print(f'total inactive female:{inactive_female}')