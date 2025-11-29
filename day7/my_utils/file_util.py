"""
文件相关的工具模块
"""

def print_file_info(file_name):
    """将指定的文件输出，不存在捕获异常并输出

    Args:
        file_name (_type_): 文件路径
    """    
    fr = None
    try:
        fr = open(f"{file_name}","r",encoding="UTF-8")
        for line in fr:
            line = line.strip()
            print(line)
    except FileNotFoundError as e:
        print(f"出现异常，问题是{e}")
    finally:
        if fr: #如果变量为none，表示false，有内容就是true
            fr.close()

def append_to_file(file_name,data):
    """将指定的数据追加到指定的文件中

    Args:
        file_name (_type_): 文件路径
        data (_type_): 指定数据
    """    
    fa = open(f"{file_name}","a",encoding="UTF-8")
    fa.write(f"{data}\n")


if __name__ == '__main__':
    print_file_info("D:/abcde.txt")
    append_to_file("d:/abcd.txt","1232312")