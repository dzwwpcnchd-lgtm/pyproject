#python异常，模块，包

#了解异常 bug 出错

#捕获异常

#基本语法
try:
    open("d:/abc.txt","r",encoding="UTF-8")
except:
    open("d:/abc.txt","w",encoding="UTF-8")    

#捕获指定异常
try:
    print(name)
except NameError as e: #只捕获nameerror这种异常 
    print("出现了变量未定义的异常") 

# 捕获多个异常
try:
    print(name)
except (NameError,ZeroDivisionError) as e:
    print("出现了变量未定义或者除以0的异常")

# 未正确设置异常类型，无法捕获异常

# 捕获所有异常
try: 
    f = open("d:/123.txt","r",encoding="UTF-8") #可能出现异常的语句
except Exception as e: #exception 所有异常都会捕获
    print("出现异常了") #出现异常的准备手段
    f = open("d:/123.txt","w",encoding="UTF-8")
else: #else 可以加也可以不加
    print("没有出现异常") #不出现异常的准备手段
finally: #有无异常都会执行
    print("有无异常都会执行") #出不出现异常都会执行的手段
    f.close()

# 异常的传递  不一定需要在异常出现的地方进行异常捕获，在高的层级也可以，因为传递性
def func1():
    print("func1 开始执行")
    num = 1/0
    print("func1结束执行")

def func2():
    print("func2 开始执行")
    func1()
    print("func2结束执行")

def main():
    try:
        func2()
    except Exception as e:
        print(f"异常出现了，出错信息是：{e}")
main()

# python模块

# 模块导入 [from 模块名]import[模块 |类|变量 |函数 |*][as 别名]

# 使用import导入time模块使用sleep功能(函数)

import time 
print("你好")
time.sleep(10)
print("我好")

# 使用from导入time的sleep功能(函数)
from time import sleep
print("你好")
sleep(5)
print("我好")

# 使用*导入time模块的全部功能

from time import *
print("你好")
sleep(5)
print("我好")

#使用as给特定功能加上别名
import time as t
print("你好")
t.sleep(5)
print(type(t.sleep(5)))
print("我好")

#自定义模块

#导入自定义模块使用
import my_module
my_module.add(1,2)

#导入不同模块的同名功能 会使用后面调用的那个
from my_module import add # +
from my_module2 import add # -
add(3,1)

#__main__变量 只有当程序是直接执行的才会进入if内部，如果是被导入的，则if无法进入
from my_module import add

#-_all__变量 限定*,指定哪些内容可以被*导入，直接使用不限定 

from my_module import *
addA(1,2)
addB(1,2)

#python包

# 创建一个包

# #导入自定义的包中的模块。并使用
import my_package.my_module1
import my_package.my_module2
my_package.my_module1.info1()
my_package.my_module2.info2()
from my_package import my_module1
from my_package import my_module2
my_module1.info1()
my_module2.info2()
from my_package.my_module1 import info1
from my_package.my_module2 import info2
info1()
info2()
from my_package import*
my_module1.info1()
my_module2.info2()

#通过_al__变量，控制import*

# 安装第三方包

#自定义包调用
from my_utils import file_util
from my_utils import str_util
file_util.print_file_info("c:/abc.txt")
file_util.append_to_file("c:/abc.txt","abcdsda")
from my_utils import str_util
str = str_util.str_reverse("abc123")
print(str)
str_util.substr("3dasd213123",0,5)