# 练习
list_name = ["zhao","qian","song","li","zhou"]

# 添加学生
list_name.append("wu")
print(f"添加学生后，列表为：{list_name}")

# 删除学生
list_name.pop(0)
list_name.remove("zhao")
print(f"删除学生后，列表为：{list_name}")

# 修改学生名字
list_name[0] = "zhen"
print(f"修改学生姓名后，列表为：{list_name}")

# 查找到某个名字的下标
index = list_name.index("song")
print(f"{list_name[index]}的下标是：{index}")

# 从列表中找出最大值（不能用 max）
def max_list(list):
    max_elemet = ""
    for element in list:
        if element > max_elemet:
            max_elemet = element
    print(f"最大值为：{max_elemet}")
max_list(list_name)

print(sorted(list_name,reverse=True)[0])

# 用列表存储 3 个学生的信息：
list_name.extend(["张三","李四","王五"])
print(f"添加三名学生后：{list_name}")

# 再写一个函数：显示所有学生名字。
def list_name_show():
    print(list_name)
list_name_show()

# 二维列表练习（重要）
# 创建一个 3×3 的表格（随便放数字），打印出来：
mylist = [[1,2,3],[4,5,6],[7,8,9]]
for element in mylist:
    print(element)

mytuple = ("wang",21,1232323)
print(mytuple,type(mytuple))

mydict = {"name":"张三","age":18,"city":"昆明"}
for element in mydict:
    print(f"{element} -> {mydict[element]}")

mydict = {"wang":{"age":18},"li":{"age":21},"zhou":{"age":24}}
def mydict_show():
    for element in mydict:
        print(f"名字是：{element}，年龄是：{mydict[element]["age"]}")

mydict_show()

#不直接用set（）去重
mylist = [1,2,3,4,5,6,2,2,2,2]
mydict1 = []
for i in mylist:
    if i not in mydict1:
        mydict1.append(i)
print(mydict1)

student_dict = {1:{"name":"张三","age":18},2:{"name":"李四","age":19}}
def show_detail():
    print("序号\t学生\t年龄")
    for key in student_dict:
        print(f"{key}\t{student_dict[key]["name"]}\t{student_dict[key]["age"]}")
def add_student():
    num = max(student_dict) + 1 
    student_dict[num] = {}  #不能直接添加，需要先设一个空的（有key值），再往里面填值
    student_dict[num]["name"] = input("输入姓名：") #可以一个一个加
    student_dict[num]["age"] = int(input("输入年龄："))
    show_detail()
def delete_student():
    name = input("输入姓名：") 
    for key in student_dict:
        if student_dict[key]["name"] == name:
            new_key = key #一边遍历一遍删除不可以，先把key值拿出来，再在外面处理
        else:
            new_key = -1
    str = student_dict.pop(new_key,"该学生不存在")    
    print(str)  
    show_detail()  #重复利用，提高代码利用率
def update_student():
    name = input("输入姓名：") 
    for key in student_dict:
        if student_dict[key]["name"] == name:
            student_dict[key]["age"] = int(input("请重新输入年龄："))
    show_detail()

while True:
    print("1. 查看")
    print("2. 添加")
    print("3. 删除")
    print("4. 修改")
    print("5. 退出")
    num = input("请输入数字：")
    if num == "1": # input输入为字符串，别忘了
        show_detail()
        continue
    elif num == "2":
        add_student()
        continue
    elif num == "3":
        delete_student()
        continue
    elif num == "4":
        update_student()
        continue
    else:
        break

#练习
students = [{"name":"张三","score":99},{"name":"李四","score":19},{"name":"王五","score":19}]

def avg_score():
    score = 0
    for element in students:
        score += element["score"]
    avg_score = score/len(students)
    print(f"平均成绩是：{avg_score}")

def max_score():
    max_score = -1
    for element in students:
       if element["score"] > max_score:
           max_score = element["score"]
           max_student = " "
           max_student = element["name"]
    # for element in students:
    #    if element["score"] == max_score:
    #         print(f"分数最高的学生是：{element["name"]}")
    print(f"分数最高的学生是：{max_student}")

def list_studet():
    student = []
    for element in students:
       if element["score"] >= 60:
           student.append(element["name"])
    print(f"成绩合格的学生有：",student)

def grade_up():
    for element in students:
        element["score"] += 5
    print(students)
    
school = {
    "class1": {"stu_num": 28, "monitor": "Xiao Ming"},
    "class2": {"stu_num": 31, "monitor": "Xiao Hong"},
    "class3": {"stu_num": 26, "monitor": "Xiao Li"}
}

def show_detail():
    for key in school:
        print(f"班级{key}有{school[key]["stu_num"]}人")

def show_monitor():
    monitors = []
    for key in school:
        monitors.append(school[key]["monitor"])
    print(f"班长列表是{monitors}")
def student_update():
    for key in school:
        num = school[key]["stu_num"]
        if num < 30:
            school[key]["stu_num"] += 2 #修改只能用这个，用变量不行
    print(school)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7}

print(a.difference(b))
print(a.union(b))
print(a.intersection(b))
#学生管理系统
student =[{"name":"tom","age":18,"score":99},{"name":"jerry","age":189,"score":80}]
def show_details():
    for element in student:
        print(f"{element}")
def add_student():
    name = input("输入姓名")
    age = input("输入年龄")
    score = input("输入成绩")
    student.append({"name":name,"age":age,"score":score})
    show_details()
def del_student():
    name = input("输入姓名")
    for element in student:
        if element["name"] == name:
            index = student.index(element)
    student.pop(index)
    show_details()
def select_student():
    name = input("输入姓名")
    for element in student:
        if element["name"] == name:
            print(f"该学生信息为：{element}")

def manu():
    while True:
        print("---学生管理系统---")
        print("1. 查看")
        print("2. 新增")
        print("3. 删除")
        print("4. 查找")
        print("5. 退出")
        num = input("输入数字：")
        if num == "1":
            show_details()
            continue
        elif num == "2":
            add_student()
            continue
        elif num == "3":
            del_student()
            continue
        elif num == "4":
            select_student()
            continue
        else:
            break 
manu()






           
        








