# a=int(input('enter the first num'))
# b=int(input('enter the sec num'))
# c=int(input('enter the third num'))
# def sum_number():
#     print(a+b+c)

# sum_number()


# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")

# num=int(input('enter the number you wana print:'))

# for i in range(num):
#     print('hello')
# def result():
#   sid=0
  
#   num=int(input('enter the number of student:'))

#   for i in range(num):
#     stu=input('enter the students name:')
#     nep =int(input("Enter Nepali marks: "))
#     eng =int(input("Enter English marks: "))
#     math =int(input("Enter Math marks: "))
#     sci =int(input("Enter Physics marks: "))
#     soc =int(input("Enter Chemistry marks: "))
#     total=(nep+eng+math+sci+soc)

#     per=total/5
#     if per>80:
#       grade='A'
#     elif per>60:
#       grade="B"
#     elif per>50:
#       grade="C"
#     elif per>40:
#       grade='D'
#     else:
#       grade='fail'
    
#     sid+=1
#     print('-----------------student result------------')
#     print('sid\t| name\t| total\t| percentage| grade\t|')
#     print(f'{sid}\t| {stu}\t| {total}\t| {per}| {grade}\t|')

  

# result()


# def total(*num):
#     total=0
#     nu=int(input('enter the number of item '))
#     for i in range(nu):
#         num=int(input('enter numbers:'))
#         total+=num
#     print(total)

# total()


# def small():
#     a=int(input('enter the first number:'))
#     b=int(input('enter the sec number:'))
#     c=int(input('enter the third number:'))
#     if a>b>c:
#         print(f'smallest= number={c}')
#     elif b>c>a:
#         print(f"smallest number = {a}")
#     elif a>c>b:
#          print(f"smallest number = {b}")
#     elif c>a>b:
#          print(f"smallest number = {b}")
#     elif c>b>a:
#          print(f"smallest number = {a}")
#     else:
#           print(f"smallest number = {c}")
# small()

# def take_mark():
#      num=int(input('enter the number of student:'))

#      for i in range(num):
#           stu=input('enter the students name:')
#           nep =int(input("Enter Nepali marks: "))
#           eng =int(input("Enter English marks: "))
#           math =int(input("Enter Math marks: "))
#           sci =int(input("Enter Physics marks: "))
#           soc =int(input("Enter Chemistry marks: "))
#           total=(nep+eng+math+sci+soc)
#      per=total/5
#      if per>80:
#           grade='A'
#      elif per>60:
#           grade="B"
#      elif per>50:
#           grade="C"
#      elif per>40:
#           grade='D'
#      else:
#           grade='fail'


# si=lambda p,t,r:p*t*r/100
# print(si(100000,2,6))






# def  products():
#      return[
#         {'pid':1,'name':'dell','price':50000,'qty':10},
#         {'pid':2,'name':'mac','price':90000,'qty':8},
#         {'pid':3,'name':'mi','price':20000,'qty':60},
#         {'pid':4,'name':'sony','price':15000,'qty':30},

#         ]
# print(products())


# def search():
#      global products
#      all_products=products()
#      num=int(input('enter the number of products you want'))
#      name=input('enter the name of product you want:')
#      for i in range(num):
#           name=input('enter the name of product you want:')
#           if name ==products['name']:
#               print(f'name:{name}\f,price:{'price'}\fstock{'qty'}')  
#           else:
#                print('the product is not available:')


def products():
    return [
        {'pid': 1, 'name': 'dell', 'price': 50000, 'qty': 10},
        {'pid': 2, 'name': 'mac', 'price': 90000, 'qty': 8},
        {'pid': 3, 'name': 'mi', 'price': 20000, 'qty': 60},
        {'pid': 4, 'name': 'sony', 'price': 15000, 'qty': 30},
    ]

def search():
    all_products = products()
    cart = []
    num = int(input('Enter the number of products you want to search for: '))
    
    for i in range(num):
        name = input(f'Enter the name of product {i+1} you want to search for: ')
        found = False
        for item in all_products:
            if item['name'].lower() == name.lower():
                print(f"Found: Name: {item['name']}, Price: {item['price']}, Available Stock: {item['qty']}")
                qty_wanted = int(input(f"Enter quantity to buy: "))
                
                if qty_wanted <= item['qty']:
                    total_price = qty_wanted * item['price']
                    cart.append({'name': item['name'], 'price': item['price'], 'qty': qty_wanted, 'total': total_price})
                    print(f"Added to bill: {qty_wanted} x {item['name']} = {total_price}")
                else:
                    print(f"Only {item['qty']} items available. Cannot add to bill.")
                found = True
                break
        if not found:
            print(f"Product '{name}' not found.")


    if cart:
        print("--- Bill ---")
        grand_total = 0
        for item in cart:
            print(f"{item['qty']} x {item['name']}  {item['price']} each = {item['total']}")
            grand_total += item['total']
        print(f"Total Amount: {grand_total}")
    else:
        print("No items purchased.")


search()



