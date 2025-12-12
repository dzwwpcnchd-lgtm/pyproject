#os导入
import os
#获取当前工作目录
current_directory = os.getcwd()
print(f"当前工作目录是：{current_directory}")
#改变当前工作目录
# os.chdir()
#列出目录内容
files_and_dirs = os.listdir()
print(f"目录内容{files_and_dirs}")
#创建目录
# os.mkdir("new_directorry")
#删除目录
# os.rmdir("new_directorry")
#删除文件
# os.remove("abc.json")
#重命名文件或目录
# os.rename("day0.py","day1.py")
#获取环境变量
home_directory = os.getenv("HOME")
print(f"{home_directory}")
#执行系统命令
# os.system("ls -l")

#---------os.path---------------
print(__file__)
# 方法
# 描述
os.path.abspath(path)
# 将相对路径转换为绝对路径。
os.path.basename(path)
# 获取路径的最后一部分，即文件名。
os.path.dirname(path)
# 获取路径中的目录部分。
os.path.join(*paths)
# 拼接多个路径，自动处理路径分隔符。
os.path.split(path)
# 将路径分割为目录和文件名的元组。
os.path.splitext(path)
# 将路径分割为文件名和扩展名的元组。
# 路径信息获取
# 方法
# 描述
os.path.exists(path)
# 判断路径是否存在。
os.path.isfile(path)
# 判断路径是否为文件。
os.path.isdir(path)
# 判断路径是否为目录。
os.path.getsize(path)
# 获取文件的大小，以字节为单位。
os.path.getatime(path)
# 获取文件的最后访问时间。
os.path.getmtime(path)
# 获取文件的最后修改时间。
os.path.getctime(path)
# 获取文件的创建时间（在某些操作系统上表示最后状态更改时间）。

#pathlib.Path  
# 是 Python 标准库中用于面向对象路径操作的核心类（自 Python 3.4 引入），
# 它取代了传统的  os.path  字符串拼接方式，提供更直观、跨平台的文件系统路径处理方式1。
# 核心特性

# 1. 面向对象设计
# 通过方法和属性操作路径，替代字符串拼接，提升代码可读性。  123
from pathlib import Path
p = Path("/home/user/file.txt")  # 创建路径对象

# 2*跨平台兼容
# 自动处理 Windows（ \ ）和 POSIX（ / ）系统的路径分隔符差异。

# 3. 路径解析便捷**
# 直接通过属性获取路径关键信息：   
print(p.name)    # 文件名: file.txt
print(p.stem)    # 无后缀名: file
print(p.suffix)  # 扩展名: .txt
print(p.parent)  # 父目录: /home/user

# 4*文件系统操作集成**
# 封装常用文件/目录操作方法：
# `python
# 目录操作
p.mkdir(parents=True, exist_ok=True)  # 递归创建目录
p.rmdir()                             # 删除空目录
# 文件操作
p.writetext("Hello", encoding="utf-8")  # 写入文件
content = p.readtext(encoding="utf-8")  # 读取文件
p.unlink()                               # 删除文件

# 5*路径遍历与匹配**

# 遍历当前目录
for item in Path.cwd().iterdir():
    print(item)

# 全局匹配文件
for py_file in Path.cwd().glob("*.py"):
    print(py_file)

# 递归匹配
for log_file in Path.cwd().rglob("*.log"):
    print(log_file)

# 与传统  os.path  对比特性 pathlib.Path  os.path 操作方式面向对象（方法/属性）字符串函数拼接路径拼接 /  运算符（ p / "subdir" ） os.path.join() 跨平台性自动处理系统差异需手动处理分隔符功能集成度包含文件读写、目录创建等操作仅路径解析，需结合  os 代码可读性更高（链式调用）较低（嵌套函数调用）典型应用场景# 创建目录并写入文件
new_dir = Path("data/logs")
new_dir.mkdir(exist_ok=True)
(new_dir / "app.log").write_text("Log started")

# 读取配置文件
config_path = Path.home() / ".config/app.ini"
if config_path.exists():
    settings = config_path.read_text()
# 总结： pathlib.Path  通过面向对象设计统一了路径操作逻辑，
# 显著提升代码简洁性与可维护性，是 Python 3.4+ 推荐的文件路径处理工具。

#--------------虚拟环境--------------------
# 在 Python 项目中使用虚拟环境可以隔离项目依赖，避免全局环境污染。
# 以下是创建 + 激活虚拟环境的完整步骤，涵盖 Windows、macOS/Linux 系统，以及不同工具（venv/conda）的用法：
# 一、核心工具：Python 内置 venv（推荐，无需额外安装）
# venv 是 Python 3.3+ 内置的虚拟环境工具，无需额外安装，是最通用的选择。
# 步骤 1：创建虚拟环境
# 进入你的项目根目录（先打开终端 / 命令提示符，cd 到项目路径），执行以下命令创建虚拟环境（默认命名为 venv，也可自定义名称）：
# bash
# 运行
# # 通用命令（Python 3 版本）
# python -m venv venv  # Windows/macOS/Linux 通用，venv 是虚拟环境文件夹名
# # 若系统同时装了 Python 2/3，需指定 python3
# python3 -m venv venv  # macOS/Linux 优先用这个
# 执行后，项目目录会生成一个 venv 文件夹，包含虚拟环境的所有依赖和解释器。
# 步骤 2：激活虚拟环境
# 激活后，终端会显示虚拟环境名称（如 (venv)），此时安装的包都会被隔离在这个环境中。
# 系统	激活命令（终端 / 命令行）
# Windows（CMD）	venv\Scripts\activate.bat
# Windows（PowerShell）	venv\Scripts\Activate.ps1（需先执行：Set-ExecutionPolicy RemoteSigned -Scope CurrentUser，按提示输入 Y 确认）
# macOS/Linux	source venv/bin/activate
# 示例（Windows CMD）：
# cmd
# # 进入项目目录
# cd D:\my_python_project
# # 激活
# venv\Scripts\activate.bat
# 激活后终端前缀会变成：(venv) D:\my_python_project>
# 步骤 3：退出虚拟环境
# 无需使用时，执行以下命令退出：
# bash
# 运行
# deactivate  # 所有系统通用
