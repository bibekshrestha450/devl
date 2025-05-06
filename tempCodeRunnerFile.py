students = [
    {'name': 'ram', 'gender': 'male', 'status': True},
    {'name': 'sophia', 'gender': 'female', 'status': False},
    {'name': 'gopal', 'gender': 'male', 'status': False},
    {'name': 'hari', 'gender': 'male', 'status': False},
    {'name': 'sita', 'gender': 'female', 'status': True}
]
total_user=0
total_male=0
total_female=0
total_active=0 
total_inactive=0
total_active_male=0
total_active_female=0
total_inactive_male=0
total_inactive_female=0

for student in students:
    total_user+=1

    if 'gender'=='male':
        total_male+=1
        if student['status']==True:
            total_active_male+=1
        else:
            total_inactive_male+=1
    else:
        total_female+=1
        if student['status']==True:
            total_active_female+=1
        else:
            total_inactive_female+=1
    if student['status']==True:
        total_active += 1
    else:
        total_inactive += 1


print("Total users:", total_user)
print("Total male:", total_male)
print("Total female:", total_female)
print("Total active users:", total_active)
print("Total inactive users:", total_inactive)
print("Total active male:", total_active_male)
print("Total active female:", total_active_female)
print("Total inactive male:", total_inactive_male)
print("Total inactive female:", total_inactive_female)
