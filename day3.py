# 黑马day3
# 判断语句
# 布尔类型，
# bool_1=True 
# bool_2=False
# print(f"bool_l内容是：{bool_1},类型是{type(bool_1)}")
# print(f"bool_2内容是：{bool_2},类型是{type(bool_2)}")
# # 比较运算符 == != > < >= <=
# # == !=
# num1 = 10 
# num2 = 10
# print(f"10 == 10的比较结果是：{num1 == num2}")

# num1 = 10 
# num2 = 15
# print(f"10 == 15的比较结果是：{num1 != num2}")

# name1 = "it"
# name2 = "it1"
# print(f"it == it1的结果是：{name1 == name2}")

# # < > <= >=
# num1 = 10 
# num2 = 15
# print(f"10大于5结果是：{num1>num2}")
# print(f"10小于5结果是：{num1<num2}")

# num1 = 10 
# num2 = 11
# print(f"10 >= 11 结果是{num1>=num2}")
# print(f"10 <= 11 结果是{num1<=num2}")

# if语句的基本格式

# age = 10
# if age >=18:
#     print("成年了")
#     print("进入")
# print("时间真快")

# #练习
# print("欢迎来到游乐场，儿童免费，成人收费。")
# age = input("请输入您的年龄：")
# if int(age) >= 18:
#     print("您已成年，游玩需补票10元。") 
# print("祝您游玩愉快")

# #if else语句
# age=int(input("输入年龄："))
# if age >= 18:
#     print("您已成年，买票10元")
# else:
#     print("您未成年，不需要缴费")
# print("祝您游玩愉快")

# #练习
# print("欢迎来到动物园。")
# height = float(input("请输入身高（cm）："))
# if height > 120:
#     print("您的身高超过120cm，游玩需要10元")
# else:
#     print("您的身高未超过120cm，游玩免费")
# print("祝您游玩愉快。")

#if elif else语句
# if int(input("请输入身高：")) < 120:
#     print("身高低于120cm，免费游玩。")
# elif int(input("请输入vip等级（1-5）：")) >= 3:
#     print("vip等级不低于3，免费游玩。")
# elif int(input("请输入今天是几号")) == 1:
#      print("今天是特惠日，可以免费游玩。")
# else:
#     print("条件全不满足，购票10元1张。")
# print("祝您游玩愉快。")

#练习  一下没想到
# num = 10
# if num == int(input("请输入第一次猜想的数字：")) :
#     print("猜对了")
# elif num ==int(input("不对，再猜一次：")) :
#     print("猜到了")
# elif num ==int(input("不对，再猜最后一次：")) :
#     print("可以啊")
# else:
#     print(f"全部猜错了，该数字是{num}")

#if嵌套
# if int(input("输入身高（cm）：")) > 120:
#     print("身高大于120，不能免费")
#     print("如果vip等级大于3，可以免费")
#     if int(input("输入vip等级（1-5）")) > 3:
#         print("vip等级大于3，可以免费")
#     else:
#         print("vip等级不够，买票10元")
# else:
#     print("欢迎你，小朋友，游玩愉快。")

# age = int(input("输入年龄：")) 
# if age < 30:
#     if age >= 18:
#         if int(input("输入入职时间（年）")) > 2:
#             print("给你一份礼物")
#         elif int(input("输入级别：")) > 3:
#             print("给你礼物")
#         else:
#             print("入职时间，级别不够，你没有礼物")
#     else:
#         print("年龄太小，你没有礼物") 
# else:
#     print("年龄太大，你没有礼物")

#猜数字
#1
# import random
# print("猜数字游戏，1-10，你有三次机会")
# num = random.randint(1,10)
# num_1 = int(input("第一次输入猜想数字："))

# if num_1 > num:  #第一次判断  大了
#     print("你失去了一次机会,大了")
#     num_2=int(input("第二次输入猜想数字："))
#     if num_2 > num:  #第一次大了-第二次判断  大了
#         print("还有一次机会，大了")
#         num_3 = int(input("第三次输入猜想数字："))
#         if num_3 > num:  #第一次大了-第二次判断  大了 -第三次判断 大了
#             print("大了，你没有机会了")
#         elif num_3 < num: #第一次大了-第二次判断 大了 -第三次判断 小了
#             print("小了，你没有机会了")
#         else: #第一次大了-第二次判断  大了 -第三次判断 等于
#             print("第三次你猜对了")
#     elif num_2 < num:  #第一次大了-第二次判断  小了
#         print("还有一次机会，小了")
#         num_3 = int(input("第三次输入猜想数字："))
#         if num_3 > num:  #第一次大了-第二次判断  小了 -第三次判断 大了
#             print("大了，你没有机会了")
#         elif num_3 < num: #第一次大了-第二次判断  小了 -第三次判断 小了
#             print("小了，你没有机会了")
#         else: #第一次大了-第二次判断  小了 -第三次判断 等于
#             print("第三次你猜对了")
#     else:  #第一次大了-第二次判断  等于
#         print("第二次你猜对了")
# elif num_1 < num:  #第一次判断分支 小了
#     print("你失去了一次机会,小了")
#     num_2=int(input("第二次输入猜想数字："))
#     if num_2 > num:  #第一次小了-第二次判断  大了
#         print("还有一次机会，大了")
#         num_3 = int(input("第三次输入猜想数字："))
#         if num_3 > num:  #第一次小了-第二次判断  大了 -第三次判断 大了
#             print("大了，你没有机会了")
#         elif num_3 < num: #第一次小了-第二次判断  大了 -第三次判断 小了
#             print("小了，你没有机会了")
#         else: #第一次小了-第二次判断  大了 -第三次判断 等于
#             print("第三次你猜对了")
#     elif num_2 < num: #第一次小了-第二次判断  小了
#         print("还有一次机会，小了")
#         num_3 = int(input("第三次输入猜想数字："))
#         if num_3 > num: #第一次小了-第二次判断  小了 -第三次判断 大了
#             print("大了，你没有机会了")
#         elif num_3 < num: #第一次小了-第二次判断  小了 -第三次判断 小了
#             print("小了，你没有机会了")
#         else: #第一次小了-第二次判断  小了 -第三次判断 等于
#             print("第三次你猜对了")
#     else: #第一次小了-第二次判断  等于
#         print("第二次你猜对了")
# else:  #第一次判断分支  等于
#     print("第一次你猜对了")

#2
# import random
# print("猜数字游戏，1-10，你有三次机会")
# num = random.randint(1,10)
# guess_num = int(input("输入你猜测的数字"))

# if guess_num == num:
#     print("第一次猜对了")
# else:
#     if guess_num >num :
#         print("大了")
#     elif guess_num <num:
#         print("小了")
#     guess_num = int(input("第二次输入你猜测的数字"))  
#     if guess_num == num:
#         print("第二次猜对了")
#     else:
#         if guess_num >num :
#             print("大了")
#         elif guess_num <num:
#             print("小了")
#         guess_num = int(input("第三次输入你猜测的数字"))  
#         if guess_num == num:
#             print("第三次猜对了")
#         else:
#             print("机会用完了")

# while循环的基础语法
# i = 0
# while 1<100:
#     print("xiaoei")
#     i += 1

# 练习
# i = 1
# s = 0
# while i <= 100:
#     s += i
#     i += 1
# print(f"1加到100为：{s}")

# while循环基础案例
# import random
# num = random.randint(1,100)
# guess_num = int(input("输入数字："))
# sum = 1
# while guess_num != num:
#     if guess_num > num:
#         print("大了")
#     elif guess_num < num:
#         print("小了")
#     guess_num = int(input("输入数字："))    
#     sum += 1
# print(f"猜到了，猜了{sum}次。")

#2
# import random
# num = random.randint(1,100)
# flag = True
# sum =0
# while flag:
#     guess_num = int(input("输入数字:"))
#     sum += 1
#     if guess_num == num:
#         print("猜对了")
#         flag = False
#     else:
#         if guess_num > num:
#             print("大了")
#         else:
#             print("小了")
# print(f"猜了{sum}次。")

# while循环的嵌套应用
# i=1
# while i<=100:
#     print(f"今天是表白第{i}天")
#     j=1
#     while j <=10:
#         print(f"第{j}支玫瑰花")
#         j += 1
#     print("小美，我喜欢你")
#     i += 1
# print(f"坚持了{i-1}天，表白成功")

# while嵌套循环案例
# \t 使多行字符串对齐
# print("hello\tworld")
# print("hurry\tup")
# 打印九九乘法表
# i =1
# while i<=9:
#     j=1
#     while j<=i:
#         print(f"{j}*{i}={j*i}\t",end="")
#         j += 1
#     print()
#     i += 1

# for循环的基础语法
# name = 'it'
# for i in name: #把name内容中每个取出赋予i临时变量 
#     print(i)
# 练习 数有几个a
# name = 'itheima is a brand of itcast'
# count = 0
# for i in name:
#     if i == 'a':
#         count += 1
# print(f"有{count}个a")

# range语句
# 1 range(num)
# for  i in range(10): #不包含10 0-9
#     print(i)
# 2 range(num1,num2)
# for i in range(5,10): #5-9
#     print(i)
# 3 range(num1,num2,step)
# for i in range(5,10,2):
#     print(i)

# #练习
# num = 20
# count = 0
# for i in range(1,num):
#     if i % 2 == 0:
#         count += 1
# print(f"有{count}个偶数。")

# #变量作用域 规范 for临时变量作用于循环内 
# for i in range(4):
#     print(i)
# print(i)

# #for循环的嵌套应用 for循环可以和while循环嵌套使用
# i = 0
# for i in range(1,101):
#     print(f"今天是表白的第{i}天")
#     for j in range(1,11):
#         print(f"送你的第{j}朵花。")
#     print("小美，我喜欢你。")
# print(f"第{i}天表白成功。")

#for循环实现九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={j*i}\t",end="")
#     print()

# #循环中断 break:直接结束循环 和continue：中断本次循环，直接进入下一次循环
# for i in range(1,4):
#     print("语句1")
#     continue
#     print("语句2")

# for i in range(1,5):
#     for j in range(1,5):
#         print("语句1",end="")
#         continue
#         print("语句2")
#     print("语句3")
# for i in range(1,5):
#     print("语句1")
#     break
#     print("语句2")
# print("语句3")

# for i in range(1,5):
#     print("语句1")
#     for j in range(1,5):
#         print("语句2")
#         break
#         print("语句3")
#     print("语句4")
# print("语句5")

#综合案例
import random
salary = 10000
for i in range(1,21):
    num = random.randint(1,11)
    if num < 5:
        print(f"员工{i}，绩效分为：{num},低于5，不发工资，下一位。")
        continue
    if salary >=1000:
        salary -= 1000
        print(f"向员工{i}发放工资1000元,账户余额还有{salary}元")    
    else:
        print("余额不足以发出工资了，下个月领取吧。")
        break





