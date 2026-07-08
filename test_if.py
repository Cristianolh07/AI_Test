
cars =['bmw','audi','xiao mi','toyota','byd']
'''
for car in cars:
    if car=='bmw' or car=='byd':
        print(car.upper())
    else:
        print(car.title())

carss=['bmw']
for car in carss:
    if car !='bmw':
        print('sorry!')
    else:
        print('good choice!')


numberx = 12
if numberx ==12:
    print('good choice!')


cars =['bmw','audi','xiao mi','toyota','byd']

car1='audi1'
if car1 not in cars:
        print('i miss audi!')
else:
        print('i like byd!')


cars =['bmw','audi','xiao mi','toyota','byd']
car2 = 'Byd'

if car2.lower() == "byd":
    print("i like "+car2)
else:
    print("i don't like "+car2)

if car2.upper() == "BD":
    print("i like "+car2)
else:
    print("i don't like "+car2)


a=11
b=12
if a>=b:
    print("a")
else:
    print("b")

cars =['bmw','audi','xiao mi','toyota','byd']
if 'bmw2' not in cars:
    print('i like bmw!')
else:
    print('i don\'t like bmw!')



alien ='greens'
if alien =='red':
    print('good red~')
elif alien =='green':
    print('good green~')
else:
    print('good other~')

aaa =['a','b','c']
if 'a' in aaa:
    print('good a~')
if 'b' in aaa:
    print('good b~')
if 'c' in aaa:
    print('good c~')



users=['a','b','c','d','e','admin']
for user in users:
    if user=='admin':
        print('hello admin, would you like to see a status report?')
    else:
        print('hello '+user+'!')

if users:
    print('hello all!')
else:
    print('no user!')
'''


users=['a','b','c','d','e','admin']
admin_user=['admin','b','c']

for user in users:
    if user in admin_user:
        print('admin in users')
    else:
        print('hi '+ user)
