#初识对象
#1.设计一个类(类比生活中:设计一张登记表)
class Student:
    name = None #记录姓名
    gender = None
    nationnality = None
    native_place = None
    age = None
#2.创建一个对象(类比生活中:打印一张登记表)
stu_1 = Student()
#3、对象属性进行赋值(类比生活中:填写表单)
stu_1.name = "王五"
stu_1.gender = "男"
stu_1.nationnality = "中国"
stu_1.native_place = "山东省"
stu_1.age = 34
#4.获取对象中记录的信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationnality)
print(stu_1.native_place)
print(stu_1.age)

#成员方法
#定义一个带有成员方法的类
class Student:
    name = None

    def say_hi(self):
        print(f"大家好，我是{self.name}，欢迎大家。")

    def say_hi2(self,msg):
        print(f"大家好，我是{self.name}，{msg}")

stu_1 = Student()
stu_1.name = "王五"
stu_1.say_hi2("12312")

stu_2 = Student()
stu_2.name = "张三"
stu_2.say_hi2("23ewqdwqd")

#补充
#self的作用
# 表示类对象本身的意思
# 只有通过self，成员方法才能访问类的成员变量
# self出现在形参列表中，但是不占用参数位置，无需理会

#类和对象
#演示类和对象的关系，即面向对象的编程套路(思想)

#设计一个闹钟类
class clock():
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

#构建2个闹钟对象并让其工作
clock1 = clock()
clock1.id = "01"
clock1.price = 12
print(f"闹钟编号是：{clock1.id}，价格是：{clock1.price}")
# clock1.ring()

clock2 = clock()
clock2.id = "02"
clock2.price = 15
print(f"闹钟编号是：{clock2.id}，价格是：{clock2.price}")
# clock2.ring()

#构造方法 __init__
#使用构造方法对成员变量赋值
class Student:
    name = None #有构造函数，成员变量可以不声明
    age = None
    tel = None

    def __init__(self,name,age,tel):
        self.name = name  #声明并赋值
        self.age = age
        self.tel = tel

stu = Student("王五",21,"123455")
print(stu.name)
print(stu.age)
print(stu.tel)

#练习
class Student:
    def __init__(self):
        for num in range(10):
            print(f"当前录入第{num+1}位学生，总共需录入{len(range(10))}位学生信息")
            self.name = input("请输入学生姓名：")
            self.age = input("请输入学生年龄：")
            self.address = input("请输入学生地址：")
            print(f"学生{num+1}信息录入完成，信息为：【学生姓名：{self.name}，年龄：{self.age}，地址：{self.address}】")

stu_1 = Student()
#range忘了，长度不知道用什么 len()

#其他内置方法
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age    
    #__str__魔术方法  把类对象转化为字符串，指定输出内容  默认输出地址
    def __str__(self):
        return f"类对象 name:{self.name}，age：{self.age}"
    
    #_lt__魔术方法 比较类对象 <,>
    def __lt__(self,other):
        return self.age < other.age
    
    #_le__魔术方法 比较类对象 <=,>=
    def __le__(self,other):
        return self.age <= other.age
    
    #eq__魔术方法 默认 == 比较地址
    def __eq__(self, other):
        return self.age == other.age
    
stu1 = Student("ww",31)
stu2 = Student("we",36)
print(stu1 == stu2) 
# print(stu1 >= stu2) 

#封装  将现实世界事物在类中描述为属性和方法，即为封装。
#定义一个类，内含私有成员变量和私有成员方法 
# 现实事物有部分属性和行为是不公开对使用者开放的。
# 同样在类中描述属性和方法的时候也需要达到这个要求，就需要定义私有成员了

class Phone:
    __couuent_voltage = 0.5  #定义 以__开头，类对象无法使用，内部可以使用
    
    def __kepp_single_core(self):
        print("以单核模式运行")
    
    def call_b_5g(self):
        if self.__couuent_voltage >= 1:
            print("5g通话开启")
        else:
            self.__kepp_single_core()
            print("电量不足，无法使用5g通话，设置为单核运行")

phone = Phone()
phone.call_b_5g()

#练习
import json
import random 
class Phone:
    __is_5g_enable = random.choice([True,False])

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭，4g开启")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

phone = Phone()
phone.call_by_5g()

#继承
#演示单继承
class Phone:
    IMEI = 2103
    producer = "dm"

    def call_by_4g(self):
        print("4g通话")

class Phone2020(Phone):
    face_id = "001"

    def call_by_5g(self):
        print("5g通话")

phone = Phone2020()
print(phone.IMEI)
phone.call_by_4g()
phone.call_by_5g()

# 演示多继承
class Phone:
    IMEI = 2103
    producer = "dm"

    def call_by_4g(self):
        print("4g通话")

class NFCReader:
    nfc_typr = "第五代"
    producer = "sa"

    def read_card(self):
        print("读卡")

    def write_card(self):
        print("写卡")

class RomoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开了")

class MyPhone(Phone,NFCReader,RomoteControl):
    pass

phone = MyPhone()
phone.call_by_4g()
phone.write_card()
phone.control() 
#演示多继承下，父类成员名一致的场景
print(phone.producer)#多继承，同名调用，先继承的会被调用，越左越先调用

#继承-复写

#定义子类，复写父类成员
class Phone:
    IMEI = None #序列号
    producer ="ITCAST" #厂商

    def call_by_5g(self):
        print("使用5g网络进行通话")

class MyPhoen(Phone):
    producer = "it"

    def call_by_5g(self):
        print("优化5g")

        #在子类，调用父类对象
        #1
        print(Phone.producer)
        Phone.call_by_5g(self)
        #2
        print(super().producer)
        super().call_by_5g()

phone = MyPhoen()
print(phone.producer)
phone.call_by_5g()

#类型注解-变量类型注解
# 基础数据类型注解
var_1: int = 10
var_2:str = "it"
var_3:bool = True

#类对象类型注解
class Student:
    pass
stu:Student = Student()

# 基础容器类型注解
my_list:list = [1,2,3]
my_tuple:tuple = (1,2,3)
my_dict:dict = {"naem":"王五"}

#容器类型详细注解
my_list:list[int] = [1,2,3]
my_tuple:tuple[int,str,bool]= (1,"itheima",True)
my_dict:dict[str,str] = {"naem":"王五"}

# 在注释中进行类型注解
var_1 = random.randint(1,10) #type : int
var_2 = json.loads('{"name":"zhansgsan"}') # type: dict[str,str]
def func():
    return 10
var_3 = func() #type : int
#类型注解的限制
var_4:str = 1

# 类型注解-函数方法注解
# 对形参进行类型注解
def add(x: int,y: int):
    return x+y

# 对返回值进行类型注解
def dunc(data:list) -> list:
    return data

# 类型注解-union类型注解
#使用union，先导包
from typing import Union

my_list:list[Union[int,str]] = [1,2,"it"]

def func(data:Union[int,str])->Union[int,str]:
    pass

#多态 多态，指的是:多种状态，即完成某个行为时，使用不同的对象会得到不同的状态
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal: Animal):
    #制造点暖音，需要传入Animal对象
    animal.speak()

#演示多态
dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)
# 抽象类
class AC:
    def cool_wind(self):
        pass

    def hot_wind(self):
        pass

    def swing_l_r(self):
        pass

class midea_AC(AC):
    def cool_wind(self):
        print("美的制冷")
    
    def hot_wind(self):
        print("美的制热")
    
    def swing_l_r(self):
        print("美的吹风")

class gree_AC(AC):
    def cool_wind(self):
        print("格力制冷")
    
    def hot_wind(self):
        print("格力制热")
    
    def swing_l_r(self):
        print("格力吹风")

def make_cool(ac:AC):
    ac.cool_wind()

midea = midea_AC()
gree = gree_AC()

make_cool(midea)
make_cool(gree)
