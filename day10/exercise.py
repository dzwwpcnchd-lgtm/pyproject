#统计文件有几行
# with open("test.txt","r",encoding="UTF-8") as f:
#     data_list = f.readlines()
#     count = 0
#     for element in data_list:
#         count += 1
#     print(f"有{count}行")
#向文件写入内容
# with open("test.txt","a",encoding="UTF-8") as f:
    # word = input("请输入：")
    # word = "\n" + word
    # f.write(word)
#备份文件
# with open("test.txt","r",encoding="UTF-8") as f:
    # data_list = f.readlines()
    # f_bak = open("test1.txt","w",encoding="UTF-8")
    # for i in data_list:
    #     f_bak.write(i)
#写代码检测用户输入是否为数字，不是数字就提示错误，但程序不崩溃
# try:    
#     word = input("请输入：")
#     if not isinstance(word,(int,float)):
#         raise TypeError("输入的不是数字")
# except TypeError as e:
#     print(f"出错了，{e}")

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        print(x_str[:-1])
        if x_str == x_str[:-1]:
            return True
        else:
            return False
        
s = Solution()
a =s.isPalindrome(121)
print(a)