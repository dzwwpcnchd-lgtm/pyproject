# 函数进阶

# 函数多返回值
def test_return():
    return 1,2,"hello"

x,y,z = test_return()
print(x,y,z)

# 函数多传参方式
def user_info(name,age,gender):
    print(f"姓名是{name}年龄是{age}性别是{gender}")

#1位置参数  需要按顺序输入
user_info("wang",21,"男")

#2关键字参数
user_info(name="wang",age=18,gender="女")
user_info(age=18,name="wang",gender="女") #打乱顺序无所谓
user_info("wang",age=18,gender="女") #可以和位置参数混用，但是位置参数要放在前面

#3缺省参数（默认）
def user_info(name,age,gender="男"): #设置默认值必须在最后，在前面，后面不设置，就会报错
    print(f"姓名是{name}年龄是{age}性别是{gender}")

user_info("li",20)
user_info("zhao",21,"女")

#不定长参数-位置不定长 *
def user_info(*args): #不定长定义的形式参数会作为元组存在，接收不定长数量的参数传入
    print(f"类型是{type(args)},内容是{args}")

user_info(1,2,"3")

#不定长参数-关键字不定长 **
def user_info(**kwargs): #不定长定义的形式参数会作为字典存在，接收不定长数量的参数传入
    print(f"类型是{type(kwargs)},内容是{kwargs}")

user_info(name="wang",age=12,gender="男")

# 匿名函数

#函数作为参数传递
def test_func(computer):
    result =  computer(1,2)
    print(f"结果是：{result},传入参数类型是：{type(computer)}")

def computer(x,y):
    return x+y

test_func(computer)

#匿名函数 lambda 自带return，无法写多行 只能用一次 lambda 传参：函数体
def test_func(computer):
    result =  computer(1,2)
    print(f"结果是：{result},传入参数类型是：{type(computer)}")

test_func(lambda x,y:x+y)

def get_max(nums):
    # max_num = None
    # for element in nums:
    #     if max_num == None:
    #         max_num = element
    #         if element > max_num:
    #             max_num = element
    #     else:
    #         if element > max_num:
    #             max_num = element
    # return max_num
    return max(nums)
student = ["1","2","3","4","5"]

#只有知道特定函数才能写出来
mystr ="Hello 123 !"
def record(str):
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0

    for element in str:
        if element.isalpha() :
            count += 1
        elif element.isdigit() :
            count1 += 1
        elif element.isspace():
            count2 += 1
        else:    
            count3 += 1
    print(f"数字数量为{count1},字母数量为:{count},空格数量为:{count2},其他数量为:{count3}")

score = [61,26,63,64,65]
def analyze_score(score):

    sum = 0
    count = 0 
    count1 = 0 
    count2 = 0 

    max_score = max(score) 
    for element in score:
        sum += element
        count += 1
        if element >= 60:
            count1 += 1
        else:
            count2 += 1

    print(f"平均分是{sum/count},最高分是：{max_score},及格人数是：{count1},不及格人数是：{count2}")

dict1 = {"name":"wang","age":12}
dict2 = {"name1":"li","age1":22}
def merge_dicts(*dicts): #读取每个键值对，放进新字典里 如果不重复的话
    dict3 = {}
    for element in dicts:
        for key in element:
            dict3[key] = element[key]
    print(dict3)

def merge_dicts1(*dicts): #俩个不动，直接整个放进新字典里
    dict3 = {}
    count = 0
    for element in dicts:
        count += 1
        dict3[count] = element
    print(dict3)

def show_info(**kwargs):
    for key in kwargs:
        print(f"{key}:{kwargs[key]}")

show_info(name="wang",age =18,score = 100)

#图书管理系统
books = [
    {"name": "Python", "author": "张三", "price": 49},
    {"name": "计算机网络", "author": "李四", "price": 59}
]

def add_book():
    name = input("输入书名：")
    author = input("输入作者名字：")
    price = input("输入价格：")
    books.append({"name":name,"author":author,"price":price})
    show_books()

def show_books():
    for element in books:
        print(element)

def del_books():
    name = input("请输入书名")
    index = 0
    for element in books:
        if element["name"] == name:
            index = books.index(element)
    books.pop(index)
    show_books()


def check_books():
    name = input("请输入书名")
    count = 0 
    for element in books:
        if element["name"] == name:
            print(f"该书信息为：{element}")
        else:
            count += 1
    if count == len(books):
        print("该书不存在")

def update_books():
    name = input("请输入书名")
    for element in books:
        if element["name"] == name:
            element["price"] = float(input("请输入修改的价格"))
    show_books()

def manu():
    while True:
        print("1.新增图书")
        print("2.查看图书列表")
        print("3.删除图书")
        print("4.搜索图书")
        print("5.修改图书价格")
        print("6.退出")
        num = input("请输入数字：")
        if num == "1":
            add_book()
            continue
        elif num == "2":
            show_books()
            continue
        elif num == "3":
            del_books()
            continue
        elif num == "4":
            check_books()
            continue
        elif num == "5":
            update_books()
            continue
        else: 
            break

manu()
      




