places=[]
while True:
    place = input("what's your favorite place? (enter 'over' to end)")
    if place == 'over':
        break  # 如果输入的是 over，就跳出循环
    places.append(place)

print('\nHere is your list:')
print(places)
print('\nLet us go to: ' + ', '.join(places))
