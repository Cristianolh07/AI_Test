"""
文件读取示例：演示 read() 与 readlines() 两种读法。

方式一（下方已注释）：read() 一次性读取整个文件，返回一个字符串。
方式二（当前使用）：readlines() 按行读取，返回字符串列表，每行末尾保留换行符。


# 方式一：read() —— 整文件读入为一个字符串
# with open('readme.txt') as xxxx:
#     aca = xxxx.read()
#     print(aca)

# 方式二：readlines() —— 逐行读入，得到行列表
with open('readme.txt') as numberss:
    bittt = numberss.readlines()

# 拼接各行：去掉每行末尾换行符后连成单个字符串
sss = ''
for bitt in bittt:
    sss += bitt.rstrip()

print(sss)


with open('learn_py.txt') as txt:
    txt_lines =txt.readlines()
for sss in txt_lines:
    print(sss.strip())


with open('learn_py.txt') as txt:
    for aaa in txt:
        print(aaa.rstrip())


with open('learn_py.txt') as txt:
    txt_lines =txt.readlines()
qqq=''
for sss in txt_lines:
    qqq +=sss.strip()
print(qqq)

qqqq=''
if "you" in qqq:
    qqqq=qqq.replace("you", "me")
print(qqqq)


with open('learn_py_c.txt','w') as write_type:
    write_type.write("OK,I love python.\n")
    write_type.write("OK,I love it.\n")



with open('learn_py_c.txt','a') as write_type:
    write_type.write("OK,I love python.\n")
    write_type.write("OK,I love it.\n")


while True:
    xxx=input("welcome,write your name,please")
    if xxx=='q':
        break
    with open("name.txt",'a') as ccc:
        ccc.write(xxx+'\n')


try:
    print(5/0)
except:
    print('sorry')


try:
    with open('name.txt') as n_len:
         contxt= n_len.read()
except FileNotFoundError:
    print('sorry')
else:
        
        numberss=contxt.split()
        xxxx=len(numberss)
        print(xxxx)




def count_file(file_name):
    try:
        with open(file_name) as n_len:
            contxt= n_len.read()
    except FileNotFoundError:
        print('sorry')
    else:
            numberss=contxt.split()
            xxxx=len(numberss)
            print(xxxx)

file_name='name.txt'
count_file(file_name)

files_name=['name.txt','learn_py_c.txt','xsd.txt']
for f_name in files_name:
     count_file(f_name)




while True:
    number1_user=input('please give me a number1')
    number2_user=input('please give me a number2')
    try:
        x=int(number1_user)
        y=int(number2_user)
    except ValueError:
        print('请输入数字！')
        continue
    ### pass
    else:
        c=x+y
        print(c)
        break
"""

import json
numbers = [1, 2, 3, 4, 5]
with open('numbers.json','w') as numbers_file:
    json.dump(numbers, numbers_file)







