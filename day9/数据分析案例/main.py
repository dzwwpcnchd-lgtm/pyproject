#综合案例
#面向对象，数据分析案例，主业务逻辑代码实现步骤:
#1.设计一个类，可以完成数据的封装

#2、设计一个抽象类，定义文件读取的相关功能，并使用了类实现具体功能


from file_define import FileReader,TextFileReader,JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

#3.读取文件，生产数据对象
test_file_reader = TextFileReader("D:/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("D:/2011年2月销售数据JSON.txt")

jan_data:list[Record] = test_file_reader.read_data()
feb_data:list[Record] = json_file_reader.read_data()

#将俩个list列表数据合并为一个
all_data:list[Record] = jan_data + feb_data

#4.进行数据需求的逻辑计算(计算每一天的销售额)
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        #当前日期有记录了，累加
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# print(data_dict)

#通过PyEcharts进行图形绘制
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys())) 
bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

bar.render("E:/每日销售额柱状图.html")











