'''
people={'name':'liu','age':22}
print(people['name'])
print(people["age"])
print(people)
ower =people['name']
ower_age=people["age"]
print(ower+"年龄是："+str(ower_age))


people['tall']=188
people['weight']=70
print(people)

students_a={}
students_a['name']='luo'
students_a['age']=44
students_a['class']='xiaoxue'
print(students_a)

if students_a['age']>30:
    students_a['class']='none'
elif students_a['age']>18:
    students_a['class']='highschool'
else:
    students_a['class']='school'

print(students_a['class'])

students_a['age']=19
if students_a['age']>30:
    students_a['class']='none'
elif students_a['age']>18:
    students_a['class']='highschool'
else:
    students_a['class']='school'

print(students_a)


liuhao={'city':'beijing','age':22,'favorite':'ball'}
print(liuhao)

favorite_number={
    'liu':7,
    'zhang':23,
    'huang':1
}
print ("zhang 最喜欢的数字是"+str(favorite_number['zhang']))
print ("liu 最喜欢的数字是"+str(favorite_number['liu']))
print ("huang 最喜欢的数字是"+str(favorite_number['huang']))


people={'name':'liu','age':22}

for s,w in people.items():
    print('\n s的值：'+s)
    print('w的值：'+str(w))


people={'name':'liu','age':22,'xsx':'dsd','a55':'344','xsx7':'dsd1','xsx3':'dsd'}


for sss in sorted(people.keys()):
    print(sss)
print('\n')
for sss in set(people.values()):
    print(sss)



people={'name':'liu','age':22}
people['son']='cirs'
people['father']='lay'
people['father2']='lay'
for a in sorted(people.keys()):
    print(a)
for a in set(people.values()):
    print(a)


revers ={'huanghe':'china','changjiang':'china','dahe':'USA'}
for he,guo in revers.items():
    print('this is '+he.title()+',it from '+guo.upper())

for he in revers.keys():
    print(he.title())

for he in revers.values():
    print(he.title())

peoples={
    'liu':'22',
    'zhang':'23',
    'huang':'1',
    'wu':'24'
}
names={'lu','zhang','huang'}

for aaa in names:
  if aaa in peoples.keys():
    print('hi '+aaa)
  else:
    print(aaa+" not in peoples")


lisss=[]
for aaa in range(10):
    new_aaa={'lu','zhang','huang'}
    lisss.append(new_aaa)


lisss_5=lisss[0:5]
print(lisss_5) 
for ssd in lisss_5:
    print(ssd)

print(len(lisss))

'''

peoples = [
    {
    'liu':'22',
    'shengao':'188',

    },
    {
    'wang':'29',
    'shengao':'133',
    }
]