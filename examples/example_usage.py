#!/usr/bin/env python3
"""
PyFileOps 使用示例
"""

import os
import tempfile
from pyfileops import FileOps


def main():
    """主函数"""
    print("PyFileOps 示例程序")
    print("=" * 50)

    # 创建临时目录
    temp_dir = tempfile.mkdtemp()
    print(f"工作目录: {temp_dir}")

    # 创建文件操作实例
    ops = FileOps

    # 1. 创建文件
    print("\n1. 创建文件")
    test_file = os.path.join(temp_dir, "example.txt")
    if ops.create_file(test_file, "这是一个示例文件内容"):
        print(f"文件创建成功: {test_file}")

    # 2. 创建自定义尾缀文件
    print("\n2. 创建自定义尾缀文件")
    custom_files = [
        os.path.join(temp_dir, "data.xyz"),
        os.path.join(temp_dir, "config.myapp"),
        os.path.join(temp_dir, "backup.old")
    ]

    for file in custom_files:
        if ops.create_file(file, f"{file} 的内容"):
            print(f"自定义文件创建成功: {file}")

    # 3. 读取文件
    print("\n3. 读取文件")
    content = ops.read_file(test_file)
    print(f"文件内容: {content}")

    # 4. 复制文件
    print("\n4. 复制文件")
    copy_file = os.path.join(temp_dir, "example_copy.txt")
    if ops.copy_file(test_file, copy_file):
        print(f"文件复制成功: {copy_file}")

    # 5. 移动文件
    print("\n5. 移动文件")
    new_file = os.path.join(temp_dir, "subdir", "moved_example.txt")
    if ops.move_file(test_file, new_file):
        print(f"文件移动成功: {new_file}")

    # 6. 列出文件
    print("\n6. 列出文件")
    files = ops.list_files(temp_dir)
    print(f"目录中的文件: {files}")

    # 7. 获取文件信息
    print("\n7. 获取文件信息")
    for file in files[:3]:  # 只显示前3个文件的信息
        info = ops.get_file_info(file)
        if info:
            print(f"{info['name']}: {info['size']} 字节, 扩展名: {info['extension']}")

    # 8. 删除文件
    print("\n8. 删除文件")
    if ops.delete_file(copy_file):
        print(f"文件删除成功: {copy_file}")

    print("\n示例程序完成!")


if __name__ == "__main__":
    main()