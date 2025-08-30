import unittest
import os
import tempfile
from pyfileops import FileOps


class TestFileOps(unittest.TestCase):
    """测试FileOps类"""

    def setUp(self):
        """设置测试环境"""
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "test.txt")
        self.test_content = "Hello, World!"

    def tearDown(self):
        """清理测试环境"""
        if os.path.exists(self.test_dir):
            import shutil
            shutil.rmtree(self.test_dir)

    def test_create_file(self):
        """测试创建文件"""
        result = FileOps.create_file(self.test_file, self.test_content)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.test_file))

        # 测试内容是否正确
        with open(self.test_file, 'r') as f:
            content = f.read()
        self.assertEqual(content, self.test_content)

    def test_create_file_with_custom_extension(self):
        """测试创建自定义尾缀文件"""
        custom_file = os.path.join(self.test_dir, "test.custom")
        result = FileOps.create_file(custom_file, "Custom content")
        self.assertTrue(result)
        self.assertTrue(os.path.exists(custom_file))

    def test_read_file(self):
        """测试读取文件"""
        with open(self.test_file, 'w') as f:
            f.write(self.test_content)

        content = FileOps.read_file(self.test_file)
        self.assertEqual(content, self.test_content)

    def test_copy_file(self):
        """测试复制文件"""
        with open(self.test_file, 'w') as f:
            f.write(self.test_content)

        copy_file = os.path.join(self.test_dir, "copy.txt")
        result = FileOps.copy_file(self.test_file, copy_file)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(copy_file))

        with open(copy_file, 'r') as f:
            content = f.read()
        self.assertEqual(content, self.test_content)

    def test_move_file(self):
        """测试移动文件"""
        with open(self.test_file, 'w') as f:
            f.write(self.test_content)

        new_file = os.path.join(self.test_dir, "new.txt")
        result = FileOps.move_file(self.test_file, new_file)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(new_file))
        self.assertFalse(os.path.exists(self.test_file))

    def test_delete_file(self):
        """测试删除文件"""
        with open(self.test_file, 'w') as f:
            f.write(self.test_content)

        result = FileOps.delete_file(self.test_file)
        self.assertTrue(result)
        self.assertFalse(os.path.exists(self.test_file))

    def test_list_files(self):
        """测试列出文件"""
        # 创建几个测试文件
        files = [
            os.path.join(self.test_dir, "test1.txt"),
            os.path.join(self.test_dir, "test2.txt"),
            os.path.join(self.test_dir, "test3.md")
        ]

        for file in files:
            with open(file, 'w') as f:
                f.write("test content")

        # 列出所有文件
        all_files = FileOps.list_files(self.test_dir)
        self.assertEqual(len(all_files), 3)

        # 按模式列出文件
        txt_files = FileOps.list_files(self.test_dir, "*.txt")
        self.assertEqual(len(txt_files), 2)

        md_files = FileOps.list_files(self.test_dir, "*.md")
        self.assertEqual(len(md_files), 1)

    def test_create_directory(self):
        """测试创建目录"""
        new_dir = os.path.join(self.test_dir, "subdir")
        result = FileOps.create_directory(new_dir)
        self.assertTrue(result)
        self.assertTrue(os.path.isdir(new_dir))

    def test_file_exists(self):
        """测试文件存在检查"""
        with open(self.test_file, 'w') as f:
            f.write(self.test_content)

        self.assertTrue(FileOps.file_exists(self.test_file))
        self.assertFalse(FileOps.file_exists(os.path.join(self.test_dir, "nonexistent.txt")))

    def test_get_file_info(self):
        """测试获取文件信息"""
        with open(self.test_file, 'w') as f:
            f.write(self.test_content)

        info = FileOps.get_file_info(self.test_file)
        self.assertEqual(info["name"], "test.txt")
        self.assertEqual(info["path"], self.test_file)
        self.assertEqual(info["extension"], ".txt")
        self.assertGreater(info["size"], 0)
        self.assertIsNotNone(info["created"])
        self.assertIsNotNone(info["modified"])


if __name__ == "__main__":
    unittest.main()