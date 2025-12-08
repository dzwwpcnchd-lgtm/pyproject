# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# class Student(Person):
#     def __init__(self, name, age,student_id):
#         self.name = name
#         self.age = age
#         self.studenta_id = student_id
    
#     def __str__(self):
#         return f"学生信息为：{self.name}{self.age}{self.studenta_id}"

# stu = Student("王五",12,"001")
# print(stu)

# '''
# 练习 2：银行账户类

# 设计类：
# 	•	deposit() 存款
# 	•	withdraw() 取款
# 	•	show_balance() 查询

# 要求：
# 	•	存款不能为负
# 	•	余额不足时要抛出异常（自定义异常）
# 	•	取款和存款都要用 try/except 做安全处理
# ''' 
# class InsufficientFundsError(Exception):
#     pass

# class BankAccount:
#     def __init__(self,money=0):
#         self.money = money
    
#     def deposit(self,in_money):
                
#         try:
            # if not isinstance(in_money, (int, float)):
            #     raise TypeError("存款金额必须是数字")
#             if in_money < 0:
#                 raise ValueError("存款不能为负")
#         except ValueError as e:
#             print(f"存款失败，{e}")
        # except isinstance as e:
        #     print(f"存款失败，{e}")
#         except Exception as e:
#             print(f"存款失败：{e}")
#         else:      
#             self.money += in_money

#             self.show_blance()
    
#     def withdraw(self,out_money):

#         try:
            # if not isinstance(out_money, (int, float)):
            #     raise TypeError("取款金额必须是数字")
#             if out_money < 0:
#                 raise ValueError("取款不能为负数")
#             if self.money < out_money:
#                 raise IndentationError("余额不足")
#         except ValueError as e:
#             print(f"取款失败，{e}")
#         except InsufficientFundsError as e:
#             print(f"取款失败，{e}")
        # except isinstance as e:
        #     print(f"取款失败，{e}")
#         except Exception as e:
#             print(f"取款失败，{e}")
#         else:
#             self.money -= out_money 
            
#             self.show_blance()
      
#     def show_blance(self):
#         print(f"存款为{self.money}")

# bankaccount = BankAccount(10000)
# # bankaccount.show_blance()
# bankaccount.deposit("abc")

# #图书类
# class Book:
#     def __init__(self,name,auther,price):
#         self.name = name
#         self.auther = auther
#         self.price = price

#     def show_info(self):
#         pass

#学生管理系统
import json

class Student:
    def __init__(self,name,age,id,score):
        self.name = name
        self.age = age
        self.id = id
        self.score = score

    def __str__(self):
        return f"{self.name},{self.age},{self.id},{self.score}"

class StudentManager:
    list_students = []

    def load_from_file(self,path):
        f= open(path,"r",encoding="UTF-8")
        for line in f.readlines():
            data_dict = json.loads(line)
            stu = Student(data_dict["name"],data_dict["age"],data_dict["id"],data_dict["score"])
            self.list_students.append(stu)
        f.close()
        return self.list_students

    def add_student(self,name,age,id,score):
        
        self.list_students.append(Student(name,age,id,score))
    
    def delete_student(self,id):

        for index,student in enumerate(self.list_students):
            if student.id == id:
                self.list_students.pop(index)
                return True
        print("此人不存在")
        return False

    def update_student(self,name,age,id,score):

        for student in self.list_students:
            if student.id == id:
                student.age = age
                student.name = name 
                student.score = score
                return True    
        print("不存在此人")
        return False
        
    def search_student(self,name):
        for student in self.list_students:
            if student.name == name:
                print(f"{student.name},{student.age},{student.id},{student.score}")

    def save_from_file(self,path):
        try:
        # 使用"w"模式覆盖写入，保证文件是完整的JSON数组
            with open(path, "w", encoding="UTF-8") as f:
                student_list = [
                    {"name": stu.name, "age": stu.age, "id": stu.id, "score": stu.score}
                    for stu in self.list_students
                ]
            # 写入JSON字符串到文件
                json.dump(student_list, f, ensure_ascii=False, indent=2)
            print("数据保存成功")
        except IOError as e:
            print(f"保存失败：文件操作错误 - {e}")
        except Exception as e:
            print(f"保存失败：{e}")


    


      

