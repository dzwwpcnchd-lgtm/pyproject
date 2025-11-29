#python day1
#----输出-------
print("hello world \n")
姓名 = "nihao"
print(姓名)
#---------标注---------
#!niahoma
#sjadksa
print("nihao")  #dasdasd

if True:
    print("true")
else:
   print("false")
   print("")
#用\连接长句子
item_one = 1
item_two = 2
item_three = 3
item_total = item_one +\
             item_two +\
             item_three
print(item_total) 
#用''' ''' 实现多行功能
a = '''  123123
       312321
           2312312
      '''
print(a) 
#--------字符串应用--------------
str='123456 '
print(str)
print(str[0::2]) #输出第一个至第三个
print(str*2) #连续输出俩条
print(str + "你好") #拼接
print('nihao\nnihao')
print (r'nihao\nnihao') #有r,不会转义\n
#-----输入--------
#input('\n\n按下enter后退出')
#用; 同一行显示多条语句
import sys;x='runoob';sys.stdout.write(x + '\n')
#------print()自动换行，end()取消换行-------
x='12'
y='34'
print(x)
print(y)
print(x,end=' ')
print(y,end=' ')
#---------导入模块---------------
import sys
print('=============python import mode============')
print('命令行参数为：')
for i in sys.argv:
    print(i)
print('\n python路径为：',sys.path) 

from sys import argv,path
print('argv是：',argv)

#------------实践任务-----------
#1
print('Hello,Python')
#2
name = ""
age = ''
name = input('请输入姓名：')
age = input('请输入年龄：')
print("姓名："+name+"\n年龄："+age)
#--------复盘------------
name = input('输入名字')
print(f"你好，{name}!")
# f{}  f-string 实现name的内嵌
try :
   age = int(input('输入年龄'))
   print('年龄是',age + 2)
except ValueError:
   print('输入有效数字')
#字符串只能连接字符串 
print('5'+'3')
print(5 + 3)





