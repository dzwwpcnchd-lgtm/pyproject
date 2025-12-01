# json 
# JSON是一种轻量级的数据交互格式。可以按照JSON指定的格式去组织和封装数据
# JSON本质上是一个带有特定格式的字符串
# 主要功能:json就是一种在各个编程语言中流通的数据格式
# 负责不同编程语言中的数据传递和交互 

#json数据和python字典的相互转换
import json
# 准备列表，列内每一个元素都是字典，将其转换为JSON
data = [{"name":"张三","age":13},{"name":"李四","age":11},{"name":"王五","age":12}]
json_str = json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)
# 准备字典，将宇典转换为JSON
d = {"name":"wang","age":11}
json_dir = json.dumps(d)
print(type(json_dir))
print(json_dir)
# 将JSON字符申转换为Python数据类型[{k:v，k:v}，{k:v，k:v}]
s = '[{"name": "张三", "age": 13}, {"name": "李四", "age": 11}, {"name": "王五", "age": 12}]'
l = json.loads(s)
print(type(l))
print(l)
# 将JSON字符串转换为Python数据类型{k:v，k:v}
s = '{"name": "张三", "age": 13}'
l = json.loads(s)
print(type(l))
print(l)

#pycharts 基础入门  折线图 
#导包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts

#创建一个折线图对象
line = Line()
#给折线图对象添加x铀的数据
line.add_xaxis(["中国","美国","英国"])
#给折线图对象添加y抽的数据
line.add_yaxis("GDP",[30,20,10])
#设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)
#用render（）方法将代码生成图像
line.render()

#折线图
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LabelOpts
#导入数据
f_us = open("D:/usshuju.txt","r",encoding="UTF-8")
us_data = f_us.read()

f_jp = open("D:/jpshuju.txt","r",encoding="UTF-8")
jp_data = f_jp.read()

f_in = open("D:/inshuju.txt","r",encoding="UTF-8")
in_data = f_in.read()

#去掉不合JSON规范的开头
us_data = us_data.replace("162934453423423","")

jp_data = jp_data.replace("162934453423424","")

in_data = in_data.replace("162934453423425","")

#去掉不合JSON规范的结尾
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

#JSON转Python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

#获取trend key
us_trend_data = us_dict["data"][0]["trend"]
jp_trend_data = jp_dict["data"][0]["trend"]
in_trend_data = in_dict["data"][0]["trend"]

# 获取日期数据，用于x轴，取2020年(到315下标结束)
us_x_data = us_trend_data["updateDate"]
jp_x_data = jp_trend_data["updateDate"]
in_x_data = in_trend_data["updateDate"]

# 获取确认数据、用于y轴，取2020年(到315下标结束)
us_y_data = us_trend_data["list"][0]["data"]
jp_y_data = jp_trend_data["list"][0]["data"]
in_y_data = in_trend_data["list"][0]["data"]

#生成图表
line = Line()
#添加x轴
line.add_xaxis(us_x_data) #x轴公用
#添加y轴
line.add_yaxis("美国人数",us_y_data,label_opts=LabelOpts(is_show=False)) #label设置是否显示y轴上的数字
line.add_yaxis("日本人数",jp_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度人数",in_y_data,label_opts=LabelOpts(is_show=False))
#全局设置
line.set_global_opts(
    title_opts=TitleOpts(title="美日印人数对比",pos_left="center",pos_bottom="1%") #标题
)
#调用render（）生成图表
line.render()
#关闭文件对象
f_us.close()
f_jp.close()
f_in.close()

#地图可视化
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
# 准备地图对象
map = Map()
# 准备数据
data = [("市",99),("市",199),("湖南省",278),("湖北省",2312),("省",2324)]
# 添加数据
map.add("测试地图",data,"china")
#全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":9,"label":"1-9", "color":"#24B1D4" },
            {"min":10,"max":99,"label":"10-99", "color":"#24D45C" },
            {"min":100,"max":999,"label":"100-999", "color":"#D4B424" },
            {"min":1000,"max":9999,"label":"1000-9999", "color":"#D45324" }
        ]

    )

)
#绘图
map.render()


#可视化地图开发-国内地图
import json
from pyecharts.charts import Map
from pyecharts.options import *
# 读取数据文件
f = open("d:/shuju.txt","r",encoding="UTF-8")
data = f.read()
#关闭文件
f.close()
#取到各省数据
#json转换为python字典
data_dict = json.loads(data) #基础数据字典
#从字典取出省份数据
province_data_list = data_dict["areaTree"][0]["children"]
#组装每个省份和确诊人数为元组、并各个省的数据都封装入列表内
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name,province_confirm))
# 创建地图对象
map = Map()
# 添加数据
map.add("各省份人数",data_list,"china")
#设置全局配置，定制分段的视觉映射
map.set_global_opts(
    title_opts=TitleOpts(title="全国地图",pos_left="center",pos_bottom="1%"),
    visualmap_opts=VisualMapOpts(
        is_show=True ,     #是否显示
        is_piecewise=True, #是否分段
        pieces=[
            {"min":1,"max":99,"lable":"1-99人","color":"#CCFFFC"},
            {"min":100,"max":999,"lable":"100-999人","color":"#D6FFCC"},
            {"min":1000,"max":9999,"lable":"1000-9999人","color":"#FFFECC"},
            {"min":10000,"max":99999,"lable":"10000-99999人","color":"#FFF3CC"},
            {"min":100000,"max":999999,"lable":"100000-999999人","color":"#FFE3CC"},
            {"min":1000000,"lable":"1000000-9999999人","color":"#FFD4CC"}
        ]

    )
)
# 绘图
map.render("E:/地图.html")

#可视化地图开发-省级地图
import json
from pyecharts.charts import Map
from pyecharts.options import *
# 读取文件
f = open("D:/shuju.txt","r",encoding="UTF-8")
data = f.read()
# 关闭文件
f.close()
# 获取河南省数据
data_dict = json.loads(data)
cities_data = data_dict["areaTree"][0]["children"][3]["children"]
# 准备数据为元组并放入list
data_list = []
for city_data in cities_data:
    city_name = city_data["name"]+"市"
    city_confirm = city_data["total"]["confirm"]
    data_list.append((city_name,city_confirm))
# 构建地图
map = Map()
map.add("各市区人数",data_list,"河南")
# 设置全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="河南省地图",pos_left="center",pos_bottom="1%"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":99,"lable":"1-99","color":"#CCFFD4"},
            {"min":100,"max":999,"lable":"100-999","color":"#F1FFCC"},
            {"min":1000,"max":4999,"lable":"1000-4999","color":"#FFF2CC"},
            {"min":5000,"max":10000,"lable":"5000-10000","color":"#FFDFCC"},
            {"min":10000,"lable":"10000-","color":"#FFD1CC"}
        ]
    )
)
# 绘图
map.render("E:\地图1.html")

#柱状图
from pyecharts.charts import Bar
from pyecharts.options import *
# 使用Bar构建基础柱状图
bar =Bar()
#添加x轴，y轴数据
bar.add_xaxis(["中国","美国","英国"])
bar.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))# 设置数值标签在右侧
# 反转x轴和y轴
bar.reversal_axis()
#绘图
bar.render("E:/Gdp.html")


#基础时间线柱状图
from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

bar1 =Bar()
bar1.add_xaxis(["中国","美国","英国"])
bar1.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 =Bar()
bar2.add_xaxis(["中国","美国","英国"])
bar2.add_yaxis("GDP",[40,25,14],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 =Bar()
bar3.add_xaxis(["中国","美国","英国"])
bar3.add_yaxis("GDP",[50,30,18],label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

#构建时间线对象
timeline = Timeline({"theme":ThemeType.LIGHT}) #设置背景，别忘了加{}
#在时间线内添加柱状图对象
timeline.add(bar1,"点1")
timeline.add(bar2,"点2")
timeline.add(bar3,"点3")
# 自动播放设置
timeline.add_schema(
    play_interval=1000, #毫秒
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
# 主题设置
# 绘图
timeline.render("E:/时间线柱状图.html")


#gdp动态柱状图绘制
#拓展sort方法
# 准备列表
my_list = [["a",33],["b",55],["c",11]]
#排序、基于带名函数
# def choose_sort_key(element):
#     return element[1]
#排序，基于lambda名函数
my_list.sort(key=lambda element:element[1],reverse=True)
print(my_list)

#实现
from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

#读取数据
f= open("D:/1960-2019全球GDP数据.csv","r",encoding="GB2312")
data_lines = f.readlines()
#文件关闭
f.close()
#删除第一条数据
data_lines.pop(0)

#将数据转换为字典存储，格式为:
#{年份:[[国家，gdp]，[国家,gdp]，…]
#{1960:[【国到 gdp],[国家,gdp],]，年份:[[国家，gdp]，[国家,gdp，......
#定义字典对象
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0]) #年份
    country = line.split(",")[1] #国家
    gdp = float(line.split(",")[2]) #GDP数据
    try:
       data_dict[year].append([country,gdp])
    except KeyError:
       data_dict[year] = []
       data_dict[year].append([country,gdp])

#创建时间线对象
timeline = Timeline({"theme": ThemeType.LIGHT})

# 排序年份
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element:element[1],reverse=True)
    year_data = data_dict[year][:8]
    x_date = []
    y_data = []
    for country_gdp in year_data:
        x_date.append(country_gdp[0]) #x轴添加国家
        y_data.append(country_gdp[1]/100000000) #y轴添加gdp数据
    
    #构建柱状图
    bar = Bar()
    x_date.reverse()
    y_data.reverse()
    bar.add_xaxis(x_date)
    bar.add_yaxis("GDP(亿)",y_data,label_opts=LabelOpts(position="right"))

    #反转x，y轴
    bar.reversal_axis()
    #设置每一年的图表标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前八gdp数据")
    )
    timeline.add(bar,str(year))

#for循环每一年的数据，基于每一年的数据，创建每一年的bar对象
#在for中，将每一年的bar对象添加到时间线中
#设置时间线自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)
#绘图
timeline.render("E:/1960-2019全球gdp前八国家.html")







