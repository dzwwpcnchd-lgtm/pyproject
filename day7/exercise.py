#读取文件内容并打印
def info():
    f = open("d:/abc.txt","r",encoding="UTF-8")
    print(f"内容为：{f.read()}")
info()

#统计文件中每个单词的次数
def word_count(filename):
    f = open(f"{filename}","r",encoding="UTF-8")
    temp_list = []
    temp_set = set()
    for line in f:
        line = line.strip()
        words = line.split(" ")
        for word in words:
            temp_list.append(word)
            temp_set.add(word)
    for element in temp_set:
        print(f"{element}:{temp_list.count(element)}")

word_count("d:/abc.txt")
#反思 
#连续使用read（），下一个会从上一个的末尾读取，
# 第一次使用俩次for循环加f.read().count(word)进行技术，得到world为0
# 才想到这个问题  第二次用集合去重，用列表收集全部元素，进行计数，成功。      

#写一个安全写文件的方法
def safe_write(path,content):
    fw = None
    try:
        fw = open(f"{path}","w",encoding="UTF-8")
        fw.write(content)
    except Exception as e:
        print(f"写文件失败，原因是：{e}")
    finally:
        fw.close()

safe_write("d:/abx.txt","hdsiah212312")