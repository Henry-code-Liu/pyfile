"""
PyFile - 文件操作核心模块
提供跨平台的文件操作功能和创建任意尾缀文件的功能
"""

import os
import shutil
import glob
from pathlib import Path
from typing import List, Union


class FileOps:
    """文件操作类"""

    @staticmethod
    def create_file(file_path: str, content: str = "") -> bool:
        """
        创建文件，支持任意尾缀

        参数:
            file_path (str): 文件路径，可以包含任意尾缀
            content (str): 文件内容，默认为空

        返回:
            bool: 成功创建返回True，否则返回False
        """
        try:
            # 确保目录存在
            directory = os.path.dirname(file_path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"创建文件时出错: {e}")
            return False

    @staticmethod
    def read_file(file_path: str) -> str:
        """
        读取文件内容

        参数:
            file_path (str): 文件路径

        返回:
            str: 文件内容
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"读取文件时出错: {e}")
            return ""

    @staticmethod
    def copy_file(src: str, dst: str) -> bool:
        """
        复制文件

        参数:
            src (str): 源文件路径
            dst (str): 目标文件路径

        返回:
            bool: 成功复制返回True，否则返回False
        """
        try:
            # 确保目标目录存在
            directory = os.path.dirname(dst)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)

            shutil.copy2(src, dst)
            return True
        except Exception as e:
            print(f"复制文件时出错: {e}")
            return False

    @staticmethod
    def move_file(src: str, dst: str) -> bool:
        """
        移动文件

        参数:
            src (str): 源文件路径
            dst (str): 目标文件路径

        返回:
            bool: 成功移动返回True，否则返回False
        """
        try:
            # 确保目标目录存在
            directory = os.path.dirname(dst)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)

            shutil.move(src, dst)
            return True
        except Exception as e:
            print(f"移动文件时出错: {e}")
            return False

    @staticmethod
    def delete_file(file_path: str) -> bool:
        """
        删除文件

        参数:
            file_path (str): 文件路径

        返回:
            bool: 成功删除返回True，否则返回False
        """
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                return True
            return False
        except Exception as e:
            print(f"删除文件时出错: {e}")
            return False

    @staticmethod
    def list_files(directory: str, pattern: str = "*") -> List[str]:
        """
        列出目录中的文件

        参数:
            directory (str): 目录路径
            pattern (str): 文件匹配模式，默认为所有文件

        返回:
            List[str]: 文件路径列表
        """
        try:
            search_pattern = os.path.join(directory, pattern)
            return glob.glob(search_pattern)
        except Exception as e:
            print(f"列出文件时出错: {e}")
            return []

    @staticmethod
    def create_directory(directory_path: str) -> bool:
        """
        创建目录

        参数:
            directory_path (str): 目录路径

        返回:
            bool: 成功创建返回True，否则返回False
        """
        try:
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
                return True
            return False
        except Exception as e:
            print(f"创建目录时出错: {e}")
            return False

    @staticmethod
    def file_exists(file_path: str) -> bool:
        """
        检查文件是否存在

        参数:
            file_path (str): 文件路径

        返回:
            bool: 文件存在返回True，否则返回False
        """
        return os.path.isfile(file_path)

    @staticmethod
    def get_file_info(file_path: str) -> dict:
        """
        获取文件信息

        参数:
            file_path (str): 文件路径

        返回:
            dict: 包含文件信息的字典
        """
        try:
            if not os.path.isfile(file_path):
                return {}

            stat = os.stat(file_path)
            return {
                "name": os.path.basename(file_path),
                "path": file_path,
                "size": stat.st_size,
                "created": stat.st_ctime,
                "modified": stat.st_mtime,
                "extension": os.path.splitext(file_path)[1]
            }
        except Exception as e:
            print(f"获取文件信息时出错: {e}")
            return {}
