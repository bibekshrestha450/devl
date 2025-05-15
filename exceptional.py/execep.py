# try:
#     print(10/2)
# except Exception as e:
#     print(e)
# finally:
#     print('done')


def add(x,y):
    if y==0:
        raise Exception('y should not be 0')
    return x+y

try:
    print(add(10,0))
except Exception as a:
    print(a)


