import time
#python 文件操作

# 文件编码 规则集合，记录文件与二进制之间转换的逻辑 常用utf-8

# 文件读取操作

# 打开文件
f = open("C:/test.txt","r",encoding = "UTF-8") #第三位不是ending，所以需要指定值
print(f"{type(f)}")

# 读取文件 read()
print(f"读取10个字节：{f.read(10)}")
print(f"读取全部内容：{f.read()}") # 在上一个read之后进行读取

# 读取文件 readLines()
lines = f.readlines() # 读取全部行 封装到列表中
print(f"lines对象的类型是{type(lines)}")
print(f"lines内容是{lines}")

# 读取文件 readLine()
lines = f.readline() # 一次读取一行 类型 str
lines1 = f.readline()
lines2 = f.readline()
print(f"lines对象的类型是{type(lines)}")
print(f"第一行内容是{lines}")
print(f"第二行内容是{lines1}")
print(f"第三行内容是{lines2}")

# for循环读取文件行
for line in f:
    print(f"每一行数据是：{line}")

# 文件的关闭
time.sleep(500000)
f.close()
time.sleep(500000)

# with open 执行完自动关闭，不会占用文件
with open("C:/test.txt","r",encoding="UTF-8") as f:
    print(f.readlines())

# 单词计数
with open("C:/test.txt","r",encoding = "UTF-8") as f:
    count = 0
    for line in f:
        count += line.count("itheima")
    print(f"有{count}个ltheima")

with open("C:/test.txt","r",encoding = "UTF-8") as f:
    count = f.read().count("itheima")
    print(f"有{count}个ltheima")

with open("C:/test.txt","r",encoding = "UTF-8") as f:
    count = 0
    for line in f:
        line = line.strip()
        words = line.split(" ")
        for word in words:
            if word == "itheima":
                count += 1
    print(f"有{count}个ltheima")

# 文件的写入

# 打开文件，不存在的文件 w模式 不存在的创建，存在的覆盖原来的内容
f = open("c:/test1.txt","w",encoding ="UTF-8")

# write写入
f.write("hello world")  #内容写入内存

#flush刷新
f.flush() # 将内存的内容写入到硬盘中

#close关闭
f.close() # 内置了flush功能

# 打开一个存在的文件
f = open("d:/test1.txt","w",encoding ="UTF-8")

# write写入，flush刷新
f.write("你好啊")

# close关闭
f.close()

#文件的追加

# 打开文件，不存在的文件 a模式 不存在的文件创建，存在的文件在原来的内容后面加
f = open("d:/test.txt","a",encoding="UTF-8")

# write写入
f.write("hello world")

#flush刷新
f.flush()

#打开一个存在的文件
f = open("d:/test.txt","a",encoding="UTF-8")
# write写入，flush刷新
f.write("\n123123123")

# close关闭
f.close()

#文件操作综合案例
with open("d:/bill.txt","r",encoding="UTF-8") as f:
    f1 = open("d:/bill.txt.bak.","w",encoding="UTF-8")
    for line in f:
        if line.count("正式") == 1:
            f1.write(line)
        else:
            continue

with open("d:/bill.txt","r",encoding="UTF-8") as f:
    f1 = open("d:/bill.txt.bak.","w",encoding="UTF-8")
    for line in f:
        line = line.strip()
        # words = line.split(",")
        # for word in words:
        #     if word == "正式":
        #         f1.write(line+"\n")
        #     else:
        #         continue
        if line.split(",")[4] == "测试":
            continue
        f1.write(line+"\n")