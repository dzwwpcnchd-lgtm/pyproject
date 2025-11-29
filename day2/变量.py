# int,float,string

# 字面量  写在代码中固定的值
# 常见  整数，浮点，字符串
# 输出各类字面量
print(666)
print(13.14)
print('黑马程序员')

'''
注释
单行 #  多行 ''' ''' 支持换行
'''

# 变量 记录数据 定义 变量名 = 变量值
money = 12
print(f'有{money}元')
print('有',money,'元')
print('有'+str(money)+'元')
money = money - 10
print('花了10元，还剩下', money)

# 练习
money = 50
print('当前钱包余额为：',money,'元')
print('购买冰淇淋，花费：',10,'元')
money = money -10
print('购买可乐，花费：',5,'元')
money = money -5
print('最终剩余：',money,'元')

# type()查看数据类型
print(type(123))
print(type('bihao'))
print(type(12.3))
#变量存储type（）结果
int_type = type(13)
print(int_type)
print(type(int_type))

#
name= 'heima'
name_type=type(name)
print(name_type)

#变量没有类型

# ------数据类型转换--------
# 数字类型转字符串类型
num_str=str(123)
print(type(num_str),num_str)

# 字符串转换为数字
num_str = int('11')
print(type(num_str),num_str)

# 错误示例  转为数字，
num3=int('heima')
print(type(num3),num3)

# 浮点型转换整数
int_num = int(11.2)
print(type(int_num),int_num) 四舍五入

# 标识符  编写代码时，对变量，类，方法编写的名字
# 1.只能使用中文，英文，数字，下划线，数字不可以开头
# 2.大小写敏感
# 3.不可以使用关键字

# 运算符
# 数学运算符
# + - * /
print('1+1=',1+1)
print('1-1=',1-1)
print('1*1=',1*1)
print('1/1=',1/1)
print('11//2=',11//2) # 整除
print('9%2=',9%2) # 取余
print('2**2=',2**2) # 指数

#赋值运算符
num = 5

#复合赋值运算符
num += 1
print('num = num + 1',num)
num -=1
print('num = num - 1',num)
num *= 2
print('num = num * 2',num)
num /= 2
print('num = num / 2',num)
num %= 2
print('num = num % 2',num)
num **= 2
print('num = num ** 2',num)
num //= 2
print('num = num // 2',num)

# 字符串拓展

# 定义 
# name = '1';name = "2"; name = ''' 3'''

# 引号嵌套 3种方法

# 1包含双引号
name = ' "nihao" '

# 2包含单引号
name = " 'niaho' "

# 3转义字符
name = " \"nihao\" "
name = ' \'nihao\' '

#字符串拼接
#字面量的拼接
print('ni'+'hao')

#字面量 ，字符串变量拼接
name = 'niaho'
print(name + 'ma?')
#无法和非字符串拼接

#字符串格式化
#%占位  %占位符 %变量
name = 'nihao'
message = 'ma,%s' % name 
print(message)

book_num = 12
food_num =2
message = '我有%s本书，%s个吃的' %(book_num,food_num)
print(message)

name = 'wang'
book_num = 12
book_prc = 10.2
message = '我从%s那里买了%d本书，每本书%f元' %(name,book_num,book_prc) # %s 把变量变成字符串放入占位的地方 %d变整数 %f变浮点数
print(message)

#格式化时精度控制  语法 m.n %3.2f等等，m，n可省略 
num1 = 11
num2 = 11.345
print('数字11宽度限制5，结果是：%5d' %num1)
print('数字11宽度限制1，结果是：%1d' %num1) #小于数字宽度，不生效
print('数字11.345宽度限制7，小数限制2，结果是：%7.2f' %num2) #小数位会四舍五入，小数点算一位
print('数字11.345小数限制2，结果是：%.2f' %num2)

#快速化字符串格式化 语法f''内容{变量}''
name = 'wang'
age = 11
print(f'我是{name},年龄{age}')

#表达式格式化 表达式：有明确结果的代码语句
1+1 ;5-2
print('1*1结果是 %d' %(1*1))
print(f'1*2的结果是{1*2}')
print('字符串在python中的类型名是%s' % type('字符串') )

#综合练习
name = '传智播'
stock_price = 19.99
stock_code = '003032'
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f'公司：{name},股票代码：{stock_code},当前股价：{stock_price}')
print('每日增长系数是：%.1f,经过%d天的增长后，股价达到了：%.2f'
       %(stock_price_daily_growth_factor,growth_days,stock_price*stock_price_daily_growth_factor**7))

#数据输入 input()语句
name = input("告诉我你是谁")
print('我知道了，你是：%s' %name )

num= input("告诉我你的银行卡密码")
print("你的银行卡密码类型是",type(num)) #无论输入什么类型数据，input接收类型是字符串类型

#练习
user_name = input('输入名字')
user_type = 'SSSSSVIP'
print(f'您好：{user_name},您是尊贵的：{user_type}用户，欢迎您的光临。')

#Bmi计算器
try :
    height = float(input('输入身高'))
    weight = float(input("输入体重"))
    bmi = ((weight/2)/((height/100)**2))
    if bmi <18.5 :
        level = 'thin'
    elif bmi > 23.9:
        level = 'fat'
    else:
        level = 'normal'
    print('体重为：%.2fkg,身高为：%.2fm,bmi为：%.2f' %((weight/2),(height/100),bmi))
    print(f'您的身高为：{height}cm，体重为：{weight}斤，健康等级为：{level}')
    print('身高为{height},体重为：{weight}，健康等级为：{level}'.format(height=height,weight=weight,level=level))
except ValueError :
    print("请输入正确的数据类型")

#闰年
age = int(input("输入年份："))
if age % 4 == 0:
    if age % 100 !=0:
        print(f"{age}是闰年")
    elif age%400 ==0:
        print(f"{age}是闰年")
    else:
        print(f"{age}不是闰年")
elif age%400 == 0:
    print(f"{age}是闰年")
else:
    print(f"{age}不是闰年")

#示例
age = int(input("输入年份："))
if (age % 4 == 0 and age % 100 != 0) or (age % 400 == 0):
    print(f"{age}是闰年")
else:
    print(f"{age}不是闰年")
