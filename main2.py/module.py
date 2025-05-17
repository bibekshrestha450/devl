# def add(x,y):
#     return x+y

# def sub(x,y):
# #     return x-y


# if __name__=="_module_":
#     print('hello')

# person1 = {
#   "name": "John",
# #   "age": 36,
#   "country": "Norway"
# }



# jobs=[
#     {'title':'python developer','exp_date':'2024-04-25'},
#     {'title':'java developer','exp_date':'2024-05-25'},
#     {'title':'data analyst','exp_date':'2025-06-25'},
#     {'title':'data scientist','exp_date':'2025-07-25'},
#     {'title':'web developer','exp_date':'2024-08-25'},
#     {'title':'android developer','exp_date':'2025-09-25'},
# ]

# import datetime

# x = datetime.datetime.now()
# print(x)
# for i in jobs:
#     if datetime<'exp_date':
#         print('available')
#     else:
# #         print('not available')

import datetime
jobs = [
    {'title': 'python developer', 'exp_date': '2024-04-25'},
    {'title': 'java developer', 'exp_date': '2024-05-25'},
    {'title': 'data analyst', 'exp_date': '2025-06-25'},
    {'title': 'data scientist', 'exp_date': '2025-07-25'},
    {'title': 'web developer', 'exp_date': '2024-08-25'},
    {'title': 'android developer', 'exp_date': '2025-09-25'},
]

x = datetime.datetime.now()
print("Current date:", x.date())

for job in jobs:
    exp_date = datetime.datetime.strptime(job['exp_date'], '%Y-%m-%d')
    if x < exp_date:
        print(f"{job['title']} - available")
    else:
        print(f"{job['title']} - not available")

# git add .
# git commit -m "Your commit message here"
# git push origin main
