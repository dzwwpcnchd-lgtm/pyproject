# heimaday4
#函数
str1 = "itheima"
str2= "itcast"
str3 = "python"

# count = 0
# for i in str1:
#     count += 1
# print(f"{str1}长度是{count}")

#使用函数优化
# def my_len(data):
#     count = 0
#     for i in data:
#         count += 1
#     print(f"{data}字符串长度为：{count}")

# my_len(str1)

#函数定义
# def say_hi():
#     print("hello world")

# say_hi()

# 练习
# def notice():
#     print("欢迎来到我的频道")

# notice()

# 函数的参数
# def add(x,y):
#     result = x + y
#     print(f"{x}+{y}的结果是：{result}.")

# add(1,2)
# add(5,6)

#练习 查体温
# def check(tem):
#     print("欢迎来查体温")
#     if tem <= 37.5:
#         print(f"体温测量中，体温为{tem},体温正常。")
#     else:
#         print(f"体温测量中，体温为{tem},体温异常，需要诊断。")

# check(36.1)
# check(38)

#函数返回值 1定义 
# def add(x,y):
#     result = x + y
#     return result
#     print("工作完成了")
# z = add(1,2)
# print(z)

#2 none类型
# def say_hi():
#     print("say hi")

# result = say_hi()
# print(result,type(result))
        
# def say_hi2():
#     print("say hi")
#     return None

# result = say_hi2()
# print(f"返回值为：{result}")
# print(f"返回类型为：{type(result)}")

# none 在if判断的应用  if判断中，none等于false，一般用于主动返回None,配合if判断做处理
# def check_age(age):
#     if age>18:
#         return "success"
#     else:
#         return None
    
# result = check_age(16)
# if not result:
#     print("未成年，不能进入网吧")

# name = None #暂时不想给初始值

# # 函数说明文档
# def add(x,y):
#     '''
#     add函数可以接收两个参数，进行俩数相加
#     x 代表其中一个参数
#     y 代表另一个参数
#     return 返回俩数相加结果
#     '''
#     result = x + y
#     print(f"{x}+{y}={result}")
#     return result
# add()

# 函数的嵌套调用
# def func_b():
#     print("-----2-----")

# def func_a():
#     print("-----1-----")
#     func_b()
#     print("-----3-----")

# func_a()

#变量的作用域
#局部变量
# def test_a():
#     num = 10 #出了函数体，不起作用
#     print(f"{num}")

# test_a()
# print(num)
#全局变量
# num =100

# def test_b():
#     print(num)

# def test_c():
#     print(num)

# test_b()
# test_c()
# print(num)

#在函数内修改全局变量
# num =100

# def test_b():
#     num = 200
#     print("test_b中num值为：",num)

# def test_c():
#     print("test_c中num值为：",num)

# test_b()
# test_c()
# print(num)

#global关键字 函数内声明变量变成全局变量
# num =100
# def test_c(): # 修改前，值没有改变
#     print("test_c中num值为：",num) 
# def test_b():
#     global num  #不能直接在这赋值
#     num = 200
#     print("test_b中num值为：",num)


# test_c()
# test_b()

# print(num)

#综合案例 ATM机
# money = 5000000
# name = input("请输入姓名：")

# def manu():
#     print(f'''----------------主菜单-------------------
# {name},您好，欢迎来到银行ATM机。请选择操作:|
# 查询余额  【输入1】                      |
# 存款      【输入2】                      |
# 取款      【输入3】                      |
# 退出      【输入4】                      |''')                    
#     return input("请输入您的选择：       ")
        
# def check_money(show_header):
#     if show_header:
#         print("--------查询余额--------")
#     print(f"{name},您好，余额为：{money}.")
    
# def in_money(in_m):
#     global money
#     money += in_m
#     print("--------存款--------")
#     print(f"{name},您好，您存款{in_m}元成功")
#     check_money(False)

# def out_money(out_m):
#     global money
#     money -= out_m
#     print("--------取款--------")
#     print(f"{name},您好，您取款{out_m}元成功")
#     check_money(False)

# while True:
#     num_1 = manu()
#     if num_1 == "1":
#         check_money(True)
#         continue
#     elif num_1 == "2":
#         in_money(float(input("请输入要存多少钱:")))
#         continue
#     elif num_1 == "3":
#         out_money(float(input("请输入要取多少钱:")))
#         continue
#     elif num_1 == "4":
#         print(f"{name},感谢使用ATM机，再见！")
#         break
#     else:
#         print("输入有误，退出程序！")
#         break

#反思
#show_header参数的使用 - 用于控制是否显示查询余额的标题部分
#重复代码的优化 - 将重复的查询余额代码封装到check_money函数中，避免代码冗余
#循环退出的优化 - 使用break语句简化循环退出逻辑，提升代码可读性
#循环内跳过某些代码的优化 - 使用continue语句跳过不必要的代码执行，提升代码效率

#练习
# def is_even(num):
#     if num % 2 == 0:
#         print(f"{num}是偶数")
#     else:
#         print(f"{num}是奇数")

# is_even(5)


# def ano_len(str):
#     count = 0 
#     for i in str:
#         count += 1
#     print(f"{str}长度为：{count}")

# str_1 = "dasdsadas"
# ano_len(str_1)

# def bigger(x,y):
#     if x > y:
#         print(f"{x}更大")
#     elif x == y:
#         print(f"{x}和{y}一样大")
#     else:
#         print(f"{y}更大")

# bigger(2,2)

# def calculator(x,y,z):
#     if y == "+":
#         print(f"{x} + {z} = {x+z}")
#     elif y == "-":
#         print(f"{x} - {z} = {x-z}")
#     elif y == "*":
#         print(f"{x} * {z} = {x*z}")
#     elif y == "/":
#         print(f"{x} / {z} = {x/z}")

# calculator(1,"/",2)

def hi(name):
    print(f"欢迎您，{name}")

hi("wang")

def bmi(height,weigit):
    Bmi = (weigit/2)/((height/100)**2)
    print
    print( ((height/100)**2))
    print("你的BMI是%.2f" %Bmi)

bmi(120,172)




