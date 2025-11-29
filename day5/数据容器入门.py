#数据容器入门 可以存储多个元素的python数据类型

#list tuple str set dirt

# list 列表 特点：1可以容纳多个数据，2可以容纳不同类型的数据。3数据是有序存储的，4允许重复数据存在，5可以修改
# 1定义 元素类型不受限制
[1,2,3,4]
my_list = ["itheima","itcast","python"]
print(my_list)
print(type(my_list))

my_list = ["itheima",666,True]
print(my_list)
print(type(my_list))

my_list = [ [1,2,3] , [4,5,6] ]
print(my_list)
print(type(my_list))

# 2列表下标索引 从前往后 0-n 从后往前 -1 - -n
my_list = ["tom","lily","rose"]
print( my_list[0])
print( my_list[1])
print( my_list[2])

#错误示范
#print(my_list[3])

print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

#嵌套列表
my_list = [ [1,2,3] , [4,5,6] ]
print(my_list[1][1])
print(my_list[-1][-2])

#3常用操作
my_list = ["itheima","itcast","python"]

#查元素下标 index（元素）
index = my_list.index("itheima")
print(f"itheima在列表中的位置为：{index}")

#元素不存在 会报错
# index = my_list.index("hello")
# print(f"itheima在列表中的位置为：{index}")

#修改指定下标的元素的值 
my_list[0] = "ithei"
print(my_list)

#元素插入 填插入后元素所在的位置 insert(下标，元素)
my_list.insert(1,"best")
print(f"列表插入元素后为，{my_list}")

#追加元素 将元素加到列表尾部
my_list.append("heimacxy")
print(f"列表追加元素后为，{my_list}")

#追加一批元素
my_list =[1,2,3]
my_list2=[4,5,6]
my_list.extend(my_list2)
print(f"mylist2加到mylist之后为：{my_list}")

#删除指定下标的元素 
#1 del列表【下标】
del my_list[0]
print(f"列表删除元素后是{my_list}")

#2 列表.pop（下标）把元素取出来，起到删除的作用 可以获取取出来的元素
element = my_list.pop(0)
print(f"列表删除元素后是{my_list},取出的元素是：{element}")

#删除某元素在列表的第一个匹配项 remove()
my_list =["heima","heima1","heima","heima1"]
my_list.remove("heima1")
print(f"删除列表的第一个'heima1'后是：{my_list}")

#清空列表
my_list.clear()
print(f"列表清空后为：{my_list}")

#统计列表中某元素数量
my_list =["heima","heima1","heima","heima1"]
print(my_list.count("heima"))

#统计列表中的元素数量
my_list =["heima","heima1","heima","heima1"]
len1 = len(my_list)
print(f"my_list长度为：{len1}")

#练习
my_list = [21,25,21,23,22,20]
my_list.append(31)
print(f"my_list追加31到尾部后为：{my_list}")
my_list.append([29,33,30]) #把列表直接加到后面
my_list.extend([29,33,30]) #把列表的元素加到后面
print(f"my_list追加31到尾部后为：{my_list}")
first_element = my_list.pop(0)
print(f"第一个元素为：{first_element}")
first_element = my_list[0]
print(f"第一个元素为：{first_element}")
last_element = my_list[-1]
print(f"最后一个元素为：{last_element}")
position = my_list.index(31)
print(my_list)
print(f"元素31的下标位置是：{position}")

# list列表的变遍历

# while循环
def list_while_func():
    my_list =[1,2,3,4,5]
    i = 0
    while i < len(my_list):
        element = my_list[i]
        print(f"第{i+1}个元素为：{element}")
        i += 1

#for 循环遍历
def list_for_func():
    my_list = [1,2,3,4,5]
    count = 0
    for i in my_list:
        count += 1
        print(f"第{count}个元素是{i}")

list_for_func()

# #练习 取出列表中的偶数
def take_for_even():
    mylist = [1,2,3,4,5,6,7,8,9,10]
    mylist1 = []
    for element in mylist:
        if element % 2 == 0:
            mylist1.append(element)
    print(f"新列表为：{mylist1}")

def take_while_even():
    mylist = [1,2,3,4,5,6,7,8,9,10]
    mylist1 = []
    index = 0
    while index < len(mylist):
        element = mylist[index]
        if element % 2 == 0:
            mylist1.append(element)
        index += 1
    print(f"新列表为：{mylist1}")

#数据容器 元组 tuple 与列表多数特性相同，但区别在于一旦定义完成，不能修改元素

#定义元组
t1 = (1,"hello",True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)},内容是{t1}")
print(f"t2的类型是：{type(t2)},内容是{t2}")
print(f"t3的类型是：{type(t3)},内容是{t3}")
t4 = ("hello",) #一个单独元素，后面要加逗号
print(f"t4的类型是：{type(t4)}")

#元组的嵌套
t5 = ((1,2,3),(4,5,6))
print(f"t5的类型是：{type(t5)},内容是{t5}")

#下标索引
print(t5[1][2])

#元组的操作：index查找方法
t6 =("it","it1","it2")
print(f"t6中it下标为：{t6.index("it")}")

#元组的操作：count统计方法
t7 =("it","it1","it2","it2","it2","it2")
print(f"t7中it2有{t6.count("it2")}个")

#元组的操作：len函数统计元组元素数量
t8 =("it","it1","it2","it2","it2","it2")
length = len(t8)
print(f"t8的长度为：{length}")

#元组的遍历：while
index = 0
while index < len(t8):
    print(f"元素为：{t8[index]}")
    index += 1

#元组的遍历：for
for element in t8:
    print(f"元素为：{element}")

#修改元组内容
t8[0] = 1

#元组中列表内的内容可以修改，列表不可以修改
t9 = (1,2,["it","it2"])
print(f"t9修改前为：{t9}")
t9[2][1] = "it3"
print(f"t9修改后为：{t9}")

# 练习 元组的基本操作
mylist = ("周杰伦",11,["football","music"])
age_index = mylist.index(11)
print(f"年龄下标为：{age_index}")
name = mylist[0]
print(f"名字是：{name}")
mylist[2].pop(0)      
mylist[2].append("coding")
print(f"修改后的元组为：{mylist}")

#数据容器 str字符串 不能修改 只能存储字符串
my_str = "itheima and itcast"

#通过下标索引取值
value = my_str[2]
value1 = my_str[-16]
print(f"下标为{2}的字符是{value}")
print(f"下标为{-16}的字符是{value1}")

my_str[2]="H"
print(my_str)

#index方法
index = my_str.index("and")
print(f"my_str中and的下标为：{index}")

#replace方法 将字符串中出现的全部字符串1全部替换为字符串2
my_str1 = my_str.replace("it","00")
print(f"{my_str}替换后为：{my_str1}")

#split方法 按指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"{my_str}用split切分后类型为：{type(my_str_list)}") 列表

#strip方法 1 字符串.strip() 去除首尾空格 2 字符串.strip(字符串) 去除首尾指定字符串 
my_str = "itheima and itcast"
my_str1 = my_str.strip()
print(f"{my_str}用strip()去除前后空格后为：{my_str1}")
my_str2 = my_str.strip("it")
print(f"{my_str}用strip(字符串)去除前后指定字符串后为：{my_str2}")

#统计字符串中某字符串的出现次数 count()
num = my_str.count("it")
print(num)

#统计字符串长度 len()
print(len(my_str))

#字符串遍历
str = "nihao"
index = 0 
while index < len(str):
    print(str[index])
    index += 1
for element in str:
    print(element)

#练习 分割字符串
str = "itheima itcast boxuegu"
num = str.count("it")
print(f"{str}有{num}个it字符串")
str_new = str.replace(" ","|")
print(f"{str}空格替换为|后为：{str_new}")
str_new_list = str_new.split("|")
print(f"{str_new}按|分割后为：{str_new_list}")

#数据容器 序列（内容连续，有序，可使用下标索引，有列表，元组，字符串）的切片
#序列【起始下标（从何处开始，可以留空，视为从头开始）：
#      结束下标（从何处结束，可以留空，视为到结尾结束）：
#      步长 1代表一个个去 2跳一个取 3跳俩个取】

#对list切片 从1开始 从4结束 步长1
my_list = [1,2,3,4,5,6,7]
new_my_list = my_list[1:4] # 步长默认为1可以不选
print(f"{my_list}切片为：{new_my_list}")

#对tuple切片 从头开始 到最后结束 步长1
my_tuple = (1,2,3,4,5,6,7)
new_my_tuple = my_tuple[:]
print(f"{my_tuple}切片为：{new_my_tuple}")

#对str切片 从头开始 到最后结束 步长2
str = "1234567"
new_str = str[::2]
print(f"{str}切片为：{new_str}")

#对str切片 从头开始 到最后结束 步长-1
new_str = str[::-1] #等于反转
print(f"{str}切片为：{new_str}，类型为：{type(new_str)}")

#对list切片 从3开始 到1结束 步长-1
my_list = [1,2,3,4,5,6,7]
new_my_list = my_list[3:1:-1]
print(f"{my_list}切片为：{new_my_list}")

#对tuple切片 从头开始 到尾结束 步长-2
my_tuple = (1,2,3,4,5,6,7)
new_my_tuple = my_tuple[::-2]
print(f"{my_tuple}切片为：{new_my_tuple}")

#序列的切片实践
str = "万过薪月,员序程马黑来,nohtyp学"
new_str = str[::-1]
new_str1 = new_str[9:14]
print(new_str1)

new_str = str[5:10]
new_str1 = new_str[::-1]
print(new_str1)

new_str = str.split(",")
new_str_list = new_str[1].replace("来","") 
new_str_list1 = new_str_list[::-1]
print(new_str_list1)

#数据容器 set 集合 不允许重复且无序,所以不支持下标索引访问

#定义
my_set = {"itheima","itcast","python","itheima","itcast","python","itheima","itcast","python"}
my_set_empty = set() #定义空集合
print(f"内容为：{my_set},类型为：{type(my_set)}")
print(f"内容为：{my_set_empty},类型为：{type(my_set_empty)}")

#添加新元素
my_set.add("jiaoyu")
print(my_set)

#移除元素
my_set.remove("itheima")
print(my_set)

#随机取出一个元素
element = my_set.pop()
print(f"取出的元素是{element},现在字符串是：{my_set}")

#清空集合
my_set.clear()
print(f"集合清空后为：{my_set}")

#取俩个集合的差集 
set1 = {1,2,3}
set2 = {1,4,5}
new_set = set1.difference(set2)
print(f"set1 和set2 的差集为：{new_set}") #1有 2没有的 不会对原来的修改
print(set1)
print(set2)

#消除俩个集合的差集
set1 = {1,2,3}
set2 = {1,4,5}
new_set = set1.difference_update(set2) #1中去掉和2相同的 
print(set1)
print(set2)

#俩个集合合并为1个
set1 = {1,2,3}
set2 = {1,4,5}
new_set = set1.union(set2)
print(new_set)
print(set1)
print(set2)

#统计集合元素数量
print(len(set1))

#集合的遍历
#不支持while循环
for element in set1:
    print(element)

#练习 信息去重
my_list = ["黑马程序员","传智播客","itcast","itheima","黑马程序员","传智播客","itcast","itheima"]
my_set = set()
for element in my_list:
    my_set.add(element)
print(f"{my_list}去重后的结果是：{my_set}")

#字典 映射 实现用key找到value的操作 key 不可以重复 不支持下标索引 可以修改 支持for 不支持while

#定义
my_dict = {"wang":99,"zhou":100,"lin":92}

#定义空字典
my_dict1 = {}
my_dict2 = dict()
print(f"内容：{my_dict}，类型：{type(my_dict)}")
print(f"内容：{my_dict1}，类型：{type(my_dict1)}")
print(f"内容：{my_dict2}，类型：{type(my_dict2)}")

#定义重复key的字典
my_dict = {"wang":99,"zhou":100,"lin":92,"lin":87,"lin":55}
print(f"内容：{my_dict}，类型：{type(my_dict)}")

#从字典基于key获取value
my_dict = {"wang":99,"zhou":100,"lin":92}
print("zhou的成绩是",my_dict["zhou"])

#定义嵌套字典 （key不可以是字典）
my_dict = {"wang":{"语文":77,"数学":66,"英语":33},"zhou":{"语文":88,"数学":86,"英语":55},"lin":{"语文":99,"数学":96,"英语":66}}

#从嵌套字典中获取数据 
print(my_dict)
print(my_dict["wang"]["语文"])

#常用操作
my_dict = {"wang":99,"zhou":100,"lin":92}

#新增元素 有就更新数据 没有就新增数据
my_dict["li"] = 87
print(f"加了li后my_dict内容为：{my_dict}")

#更新元素
my_dict["zhou"] = 91
print(f"修改了zhou成绩后，my_dict内容为：{my_dict}")

#删除元素
value = my_dict.pop("zhou")
print(f"zhou 作弊成绩为：{value},取消成绩后，成绩表为：{my_dict}")

#清空元素
my_dict.clear()
print(my_dict)

#获取全部key
my_dict = {"wang":99,"zhou":100,"lin":92}
keys = my_dict.keys()
print(f"my_dict中的key值有：{keys}")

#遍历字典

#1通过获取全部的key来完成遍历
for key in keys:
    print(f"{key}:{my_dict[key]}")

#2
for key in my_dict:
    print(f"{key}:{my_dict[key]}")

#统计字典中元素数量
lenth = len(my_dict)
print(lenth)

#练习 升职加薪
my_dict = {"wang":{"部门":"科技部","工资":3000,"级别":1},
           "zhou":{"部门":"市场部","工资":5000,"级别":2},
            "lin":{"部门":"市场部","工资":7000,"级别":3},
            "zhang":{"部门":"科技部","工资":4000,"级别":1},
            "liu":{"部门":"市场部","工资":6000,"级别":2}}
print("全体员工当前信息如下：")
print(my_dict)
for key in my_dict:
    level = my_dict[key]["级别"]
    salary = my_dict[key]["工资"]
    if  level == 1:
        my_dict[key]["级别"] += 1
        my_dict[key]["工资"] += 1000
    
print("全体员工级别为1的员工完成升职加薪操作后信息如下")
print(my_dict)

# 数据容器通用操作
mylist = [1,2,3,4,5]
mytuple = (1,2,3,4,5)
mystr = "12345"
myset = {1,2,3,4,5}
mydict = {"wang":1,"lin":2}

# len元素个数
print(f"列表有{len(mylist)}个元素")
print(f"元组有{len(mytuple)}个元素")
print(f"字符串有{len(mystr)}个元素")
print(f"集合有{len(myset)}个元素")
print(f"字典有{len(mydict)}个元素")

# max最大元素
print(f"列表最大元素是{max(mylist)}，类型为{type(max(mylist))}")
print(f"元组最大元素是{max(mytuple)}")
print(f"字符串最大元素是{max(mystr)}")
print(f"集合最大元素是{max(myset)}")
print(f"字典最大元素是{max(mydict)}")

# min最小元素
print(f"列表最小元素是{min(mylist)}")
print(f"元组最小元素是{min(mytuple)}")
print(f"字符串最小元素是{min(mystr)}")
print(f"集合最小元素是{min(myset)}")
print(f"字典最小元素是{min(mydict)}")

# 类型转换：容器转列表
print(f"列表转列表的结果是：{list(mylist)}")
print(f"元组转列表的结果是：{list(mytuple)}")
print(f"字符串转列表的结果是：{list(mystr)}")
print(f"集合转列表的结果是：{list(myset)}")
print(f"字典转列表的结果是：{list(mydict)}")  

# 类型转换：容器转元组  
print(f"列表转元组的结果是：{tuple(mylist)}")
print(f"元组转元组的结果是：{tuple(mytuple)}")
print(f"字符串转元组的结果是：{tuple(mystr)}")
print(f"集合转元组的结果是：{tuple(myset)}")
print(f"字典转元组的结果是：{tuple(mydict)}")   

# 类型转换：容器转字符串
print(f"列表转字符串的结果是：{str(mylist)}")
print(f"元组转字符串的结果是：{str(mytuple)}")
print(f"字符串转字符串的结果是：{str(mystr)}")
print(f"集合转字符串的结果是：{str(myset)}")
print(f"字典转字符串的结果是：{str(mydict)}")  

# 类型转换：容器转集合 
print(f"列表转集合的结果是：{set(mylist)}")
print(f"元组转集合的结果是：{set(mytuple)}")
print(f"字符串转集合的结果是：{set(mystr)}")
print(f"集合转集合的结果是：{set(myset)}")
print(f"字典转集合的结果是：{set(mydict)}") 

# sorted() 排序后变成列表
print(f"列表sort排序完结果是：{sorted(mylist,reverse=True)}")
print(f"元组sort排序完结果是：{sorted(mytuple,reverse=True)}")
print(f"字符串sort排序完结果是：{sorted(mystr,reverse=True)}")
print(f"集合sort排序完结果是：{sorted(myset,reverse=True)}")
print(f"字典sort排序完结果是：{sorted(mydict,reverse=True)}")

# 字符串大小比较  一位一位比，其中一位大，后面就无需比较，单个字符看asc||码
print(f"abd 大于 abc 结果{"abd">"abc"}")
print(f"ab 大于 a 结果{"ab">"a"}")
print(f"a 大于 A 结果{"a">"A"}")