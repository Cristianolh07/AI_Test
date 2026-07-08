'''
car = input("what is you favorite number?")
car =int(car)
if car % 3== 0:
    print('i like it!')
else:
    print(str(car)+' is a good choice!')

xxx={}
while True:
    number = input("what is you favorite number?")
    car = input("what is you favorite car?") 
    xxx[number]=car
    question=input("do you want to continue?")
    if question!='yes':
        break
print(xxx)


food =['Asandwich','Bsandwich','Csandwich','Csandwich','Csandwich']
finished_food=[]
while 'Csandwich' in food:
    food.remove('Csandwich')

print(finished_food)
print(food)


places=[]
while True:
    place = input("what's your favorite place? (enter 'over' to end)")
    if place == 'over':
        break
    places.append(place)

print('\nHere is your list:')
print('\nLet us go to: ' + ', '.join(places))

'''
