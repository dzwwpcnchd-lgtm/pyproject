from pathlib import Path
import os.path
import shutil
import logging

def list_files(path):
    # file = os.listdir()
    # print(f"文件为：{file}")
    try:
        p = Path(path)
        for item in p.iterdir():
            print(item)
    except Exception as e:
        print(f"出错了，错误为：{e}")

def make_dir(path):
    # os.mkdir(f"{name}")
    try:
        p = Path(path)
        p.mkdir()
    except Exception as e:
        print(f"出错了，错误为：{e}")

def del_file(path):
    # if os.path.isfile(f"{name}"):
    #     os.remove(f"{name}")
    # elif os.path.isdir(name):
    #     os.rmdir(f"{name}")
    # else:
    #     print(f"{name}不存在")
    # work_path = Path().cwd().resolve()
    # target_path = Path(path).resolve()
    
    # if work_path in target_path.parents or target_path == work_path:
    #     if target_path.is_dir():
    #         target_path.rmdir()
    #     elif target_path.is_file():
    #         target_path.unlink()
    #     else:
    #         print(f"{path}不存在")
    # else:
    #     print(f"不能删除工作目录之外的内容：{path}")
    try:
        p = Path(path)
        if p.is_dir():
            # shutil.rmtree(p)
            p.rmdir()
        elif p.is_file():
            p.unlink()
        else:
            print(f"{path}不存在")
    except Exception as e:
        print(f"出错了，错误为：{e}")

def read_file(path):
    # with open(f"{name}","r",encoding="UTF-8") as f:
    #     content = f.read()
    #     print(content)

    # p = Path(path)
    # print(p.read_text(encoding="UTF-8"))
    try:
        p = Path(path)
        content = p.read_text(encoding="UTF-8")
        print(content)  # 保留打印功能
        return content  # 新增返回内容
    except Exception as e:
        print(f"出错了，错误为：{e}")

def write_file(path,text):
    # with open(f"{name}","a",encoding="UTF-8") as f:
    #     f.write(text)
    try:
        p = Path(path)
        p.write_text(text,encoding="UTF-8")
    except Exception as e:
        print(f"出错了，错误为：{e}")

#基础配置（全局生效）
logging.basicConfig(
    level=logging.INFO, # 输出 >= info的日志
    format="%(asctime)s -%(name)s - %(levelname)s - %(message)s", # 日志格式
    datefmt="%Y-%m-%d %H:%M:%S", # 时间格式
    handlers=[
        logging.StreamHandler(), # 输出到控制台
        logging.FileHandler("file_manager.log",encoding="UTF-8") # 输出到文件
    ]
)
#获取logging实例 __name__对应模块名
logger = logging.getLogger(__name__)

#输出不同级别日志
logger.debug("调试信息，初始化配置完成")
logger.info("普通信息，用户登录成功")
logger.warning("警告信息，磁盘空间不足")
logger.error("错误信息，数据库连接失败")
logger.critical("严重错误，程序无法启动，核心配置缺失")