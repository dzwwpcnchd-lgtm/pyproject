import os.path
from pathlib import Path

path = "E:/ProgramFiles3/python_projects/pyproject/day11/exercise"
print(f"绝对路径是：{os.path.abspath(path)}")
print(f"父目录是：{os.path.dirname(path)}")

# print(os.listdir(path))
if os.path.exists(path) and os.path.isdir(path):

    for item in os.listdir(path):
        item_path = os.path.join(path,item)

        if os.path.isdir(item_path):
            print(f"目录是：{item_path}")
        elif os.path.isfile(item_path):
            print(f"文件是：{item_path}")
        else:
            print(f"其他：{item_path}") 
else:
    print(f"{path}不是有效目录")

with os.scandir(path) as entiries:
    for entry in entiries:
        print(f"{entry.name}:{'目录'if entry.is_dir() else '文件'} - {entry.path}")

p = Path("E:/ProgramFiles3/python_projects/pyproject/day11/exercise")
print(f"绝对路径是：{p.absolute()}")
print(f"父目录是:{p.parent}")
# print(type(p.iterdir()))

for item in p.iterdir():
    if item.is_dir():
        print(f'目录是：{item}')
    elif item.is_file():
        print(f'文件是：{item}')
