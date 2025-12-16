from modules import file_ops

while True:
    print("1.查看文件")
    print("2.创建文件夹")
    print("3.删除文件")
    print("4.读取文件")
    print("5.写入文件")
    print("6.退出")
     
    num = int(input("输入数字"))
    try:
        if num == 1:
                file_ops.list_files(input("输入文件名"))
        if num == 2:
                file_ops.make_dir(input("输入文件名"))
        if num == 3:
                file_ops.del_file(input("输入删除的文件名"))
        if num == 4:
                file_ops.read_file(input("输入读取的文件名"))
        if num == 5:
                file_ops.write_file(path=input("输入文件名"),text=input("输入内容"))
        if num == 6:
                break
    except Exception as e:
        print(f"出错了{e}")


    


