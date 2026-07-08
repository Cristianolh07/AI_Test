'''
def hello(names):
    print('hello !'+names)
hello('k')
hello('')


def book(title,anthor):
    print('i like '+title+' ! It is written by '+anthor)
book('xxxxx','liu')
book(title='what',anthor='xiao')
'''
'''
def make_shirt(size,types):
    print("you will make a T-shirt,size is "+size+', types is '+types)
make_shirt('xl','red')

def make_shirt(size='xxl',types='red'):
    print("you will make a T-shirt,size is "+size+', types is '+types)
make_shirt('xl','redss')

def make_shirt(size,types='red'):
    print("you will make a T-shirt,size is "+size+', types is '+types)
make_shirt('l','gray')
make_shirt('ll')
'''
'''
def city_country(name,country):
    aaa=name+" in "+country
    return aaa.title()
lll=city_country('beijing','china')
print(lll)

xxx={}
def music_band(Pname,Zname):
    p=input("ni de mingzi")
    z=input("zhuanji")
    xxx[p]=z
    print(xxx)
 
def xxxx(Pname,Zname,numbers=''):
    zj={'pname':Pname,'zname':Zname}
    if numbers:
        zj['numbers']=numbers
    return zj
zjj=xxxx('k','liu','123456')
print(zjj)
zjj=xxxx('d','question ')
print(zjj)

def xxxx(Pname,Zname):
    aaa= Pname+' '+Zname
    return aaa.title()
while True:
    P=input("ni de mingzi")
    if P=='q':
        break
    Z=input("zhuanji")
    if Z=='q':
        break
    zj=xxxx(P,Z)
    
    print("hello+ "+zj)
    

show_mags =['a','b','c']
great_mags=[]
def make_great(xxx):
    while xxx:
        yyy=xxx.pop()
        zzz='graet_'+yyy
        great_mags.append(zzz)

make_great(show_mags[:])
print(show_mags)
print(great_mags)

name_k=['k','li','d']
great_name=[]

def mags(name_kk,great_name):
    while name_kk:
        yy=name_kk.pop()
        zz='great__'+yy
        great_name.append(zz)
        print(yy+' 变形中')

def great(great_name):
    for name in great_name:
        print(name)

mags(name_k[:],great_name)
great(great_name)
print(name_k)


def sandwich(*needss):
    print('your sandwich have: ')
    for need in needss:
        print('--'+need)

sandwich('a','b','c')
'''
def someone(name,age,**informations):
    inf={}
    inf['name']=name
    inf['age']=age
    for a,b in informations.items():
        inf[a]=b
    return inf


aa=someone('k','18',sex='male',hobby='play',heavy='150kg')
print(aa)