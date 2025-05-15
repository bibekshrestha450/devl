import re

fullname='ram123'

paterns="^[A-Za-z][3]"

if re.match(paterns,fullname):
    print('valid')
else:
    print('invalid name')
    