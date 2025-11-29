'''
字符串相关的工具模块
'''

def str_reverse(s):
    """实现字符串反转功能

    Args:
        s (_type_): 将被反转的字符串

    Returns:
        _type_: 反转后的字符串
    """    
    return s[::-1]

def substr(s,x,y):
    """字符串切片

    Args:
        s (_type_): 指定字符串
        x (_type_): 开始位置
        y (_type_): 结束位置
    """    
    print(f"切片后的结果是：{s[x:y]}")

if __name__ == '__main__':
    print(str_reverse("你好啊"))
    print(substr("12345",1,4))