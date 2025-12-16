import os
import sys 
from pathlib import Path
import pytest

# 获取当前测试文件的目录（test/）
test_dir = Path(__file__).parent
# 获取 file_manager 目录（test/ 的父目录）
project_dir = test_dir.parent
# 将 file_manager 加入 Python 搜索路径
sys.path.append(str(project_dir))

from modules.file_ops import make_dir, write_file, read_file, del_file

def test_make_dir(tmp_path):
    """测试创建目录功能"""
    # 在临时目录下创建新目录
    new_dir = tmp_path / "test_dir"
    make_dir(new_dir)
    
    # 验证目录是否创建成功
    assert new_dir.exists()
    assert new_dir.is_dir()

def test_write_read_roundtrip(tmp_path):
    """测试写入和读取文件的一致性"""
    test_file = tmp_path / "test.txt"
    test_content = "Hello, 测试内容！\nSecond line"
    
    # 写入文件
    write_file(str(test_file), test_content)
    
    # 读取文件并验证内容
    assert test_file.exists()
    assert test_file.is_file()
    assert read_file(str(test_file)) == test_content  # 注意：原read_file函数需要修改为返回内容而非直接打印

def test_delete_file(tmp_path):
    """测试删除文件功能"""
    test_file = tmp_path / "to_delete.txt"
    test_file.write_text("临时内容")  # 先创建文件
    
    # 验证文件存在
    assert test_file.exists()
    
    # 删除文件
    del_file(str(test_file))
    
    # 验证文件已删除
    assert not test_file.exists()

def test_delete_directory(tmp_path):
    """测试删除目录功能"""
    test_dir = tmp_path / "to_delete_dir"
    test_dir.mkdir()  # 先创建目录
    (test_dir / "inner.txt").write_text("内部文件")  # 目录内创建文件会导致删除失败，用于测试边界情况
    
    # 验证目录存在
    assert test_dir.exists()
    
    # 尝试删除非空目录（原函数会失败，因为rmdir不能删除非空目录）
    try:
        del_file(str(test_dir))
    except Exception as e:
        print(f"不能删除非空目录{e}")
    assert  test_dir.exists()  # 非空目录应该删除失败
    
    # 清空目录后再试
    (test_dir / "inner.txt").unlink()
    del_file(str(test_dir))
    assert not test_dir.exists()  # 空目录应该删除成功

def test_write_read_special_chars(tmp_path):
    """测试特殊字符的写入读取一致性"""
    test_file = tmp_path / "special_chars.txt"
    special_content = "特殊字符测试：!@#$%^&*()_+{}|:\"<>?`~ 中文标点，。；‘’“”【】"
    
    write_file(str(test_file), special_content)
    assert read_file(str(test_file)) == special_content  # 同样需要read_file返回内容