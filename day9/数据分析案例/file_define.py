#文件相关的类定义

#定义一个抽象类做顶层设计确定有哪些功能需要实现
from data_define import Record
import json

class FileReader:
    def read_data(self)->list[Record]:
        #读取文件数据，每一条数据转换成record对象，将它们封装到list内返回
        pass 

class TextFileReader(FileReader):

    def __init__(self,path):
        self.path = path #定义成员变量，记录文件位置

    #实现抽象方法
    def read_data(self):
        f= open(self.path,"r",encoding="UTF-8")
        record_list:list[Record] = []
        for line in f.readlines():
            line = line.strip() #消除\n
            data_list = line.split(",")
            record = Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            record_list.append(record)
        
        f.close()
        
        return record_list

class JsonFileReader(FileReader):
    def __init__(self,path):
        self.path = path #定义成员变量，记录文件位置

    def read_data(self):
        f= open(self.path,"r",encoding="UTF-8")
        record_list:list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
            record_list.append(record)
        
        f.close()
        
        return record_list
        
        
if __name__ == '__main__':
    textfilereader = TextFileReader("D:/2011年1月销售数据.txt")
    jsonfilereader = JsonFileReader("D:/2011年2月销售数据JSON.txt")
    list1 = textfilereader.read_data()
    list2 = jsonfilereader.read_data()

    for l in list1:
        print(l)
    for l in list2:
        print(l)