import json
from exercise import StudentManager, Student

def test_student_manager():
    # 初始化学生管理器
    manager = StudentManager()
    test_file = "test_students.json"

    # 测试添加学生
    print("=== 测试添加学生 ===")
    manager.add_student("张三", 18, "001", 90)
    manager.add_student("李四", 19, "002", 85)
    print(f"添加后学生数量: {len(manager.list_students)} (预期: 2)")

    # 测试查询学生
    print("\n=== 测试查询学生 ===")
    print("查询张三:")
    manager.search_student("张三")  # 应输出张三的信息
    print("查询王五:")
    manager.search_student("王五")  # 无输出（不存在）

    # 测试更新学生
    print("\n=== 测试更新学生 ===")
    update_success = manager.update_student("张三", 19, "001", 95)  # 更新张三的年龄和成绩
    print(f"更新001是否成功: {update_success} (预期: True)")
    print("更新后张三的信息:")
    manager.search_student("张三")  # 年龄应为19，成绩应为95
    
    update_fail = manager.update_student("王五", 20, "003", 80)  # 更新不存在的学生
    print(f"更新003是否成功: {update_fail} (预期: False)")



    # 测试从文件加载学生
    print("\n=== 测试从文件加载学生 ===")
    new_manager = StudentManager()
    loaded_students = new_manager.load_from_file(test_file)
    print(f"加载的学生数量: {len(loaded_students)} (预期: 2)")
    print("加载的第一个学生信息:")
    print(loaded_students[0])  # 应输出更新后的张三信息

    # 测试删除学生
    print("\n=== 测试删除学生 ===")
    delete_success = new_manager.delete_student("002")  # 删除李四
    print(f"删除002是否成功: {delete_success} (预期: True)")
    print(f"删除后学生数量: {len(new_manager.list_students)} (预期: 1)")
    
    delete_fail = new_manager.delete_student("003")  # 删除不存在的学生
    print(f"删除003是否成功: {delete_fail} (预期: False)")

        #测试保存学生到文件
    print("\n=== 测试保存学生到文件 ===")
    manager.save_from_file(test_file)
    # 验证文件内容
    with open(test_file, "r", encoding="UTF-8") as f:
        saved_data = json.load(f)
    print(f"保存的学生数量: {len(saved_data)} (预期: 2)")

if __name__ == "__main__":
    test_student_manager()