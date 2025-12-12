from pathlib import Path
import os.path

def list_files():
    file = os.listdir()
    print(f"文件为：{file}")

def make_dir(name):
    os.mkdir(f"{name}")

def del_file(name):
    if os.path.isfile(f"{name}"):
        os.remove(f"{name}")
    elif os.path.isdir(name):
        os.rmdir(f"{name}")
    else:
        print(f"{name}不存在")

def read_file(name):
    with open(f"{name}","r",encoding="UTF-8") as f:
        content = f.read()
        print(content)

def write_file(name,text):
    with open(f"{name}","a",encoding="UTF-8") as f:
        f.write(text)
