# students=[
#     {'name':'ram','address':'ktm'},
#     {'name':'sita','address':'ktm'},
#     {
#         'name':'shyam',
#         'address':'ktm',
#         'contact':{
#             'phone':987687,
#             "email":'shyam@gmail.com'

#         }
#     }
# ]



# number=int(input("enter number:"))
# if number %3==0 and number %5==0:
#     print(number,"is divisiable by 3 and 5")
# else:
#     print(number, "isnot divisiable of 3 and 5")

students = [
    {'name': 'ram', 'address': 'ktm'},
    {'name': 'sita', 'address': 'ktm'},
    {'name': 'hari', 'address': 'ktm'},
    {'name': 'gita', 'address': 'ktm'}
]

for student in students:
    print('My name is', student['name'])
