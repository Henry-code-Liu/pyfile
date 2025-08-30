# PyFile - 轻量级 Python 文件操作库

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

PyFile 是一个专为 Python 开发者设计的轻量级文件操作库，提供了简单易用的 API 来处理各种文件操作任务，特别专注于创建任意尾缀的文件和基础文件管理功能。

## ✨ 特性

- 🚀 **创建任意尾缀文件** - 支持创建自定义扩展名的文件
- 📁 **完整的文件操作** - 读取、写入、复制、移动、删除文件
- 📂 **目录管理** - 创建目录、列出文件
- 🔍 **文件信息** - 获取文件大小、创建时间、修改时间等信息
- 🧪 **全面测试** - 包含完整的单元测试套件
- 📚 **详细示例** - 提供丰富的使用示例
- 🛡️ **类型提示** - 完整的类型注解，提高开发体验
- 🌐 **跨平台兼容** - 支持 Windows、macOS 和 Linux 系统

## 安装

### 从源代码安装

```bash
git clone https://github.com/yourusername/pyfile.git
cd pyfile
pip install -e .
```
## 快速开始

```python
from pyfile import FileOps

# 创建普通文本文件
FileOps.create_file("example.txt", "Hello, World!")

# 创建自定义尾缀文件
FileOps.create_file("data.xyz", "自定义格式的内容")
FileOps.create_file("config.myapp", "应用程序配置")

# 读取文件内容
content = FileOps.read_file("example.txt")
print(content)  # 输出: Hello, World!

# 复制文件
FileOps.copy_file("example.txt", "example_copy.txt")

# 移动文件
FileOps.move_file("example.txt", "backup/example.txt")

# 删除文件
FileOps.delete_file("example_copy.txt")
```

## 核心功能

### 文件操作
- `create_file(file_path, content="")` - 创建文件（支持任意尾缀）
- `read_file(file_path)` - 读取文件内容
- `copy_file(src, dst)` - 复制文件
- `move_file(src, dst)` - 移动/重命名文件
- `delete_file(file_path)` - 删除文件
- `file_exists(file_path)` - 检查文件是否存在

### 目录操作
- `create_directory(directory_path)` - 创建目录
- `list_files(directory, pattern="*")` - 列出目录中的文件

### 文件信息
- `get_file_info(file_path)` - 获取文件详细信息（大小、创建时间、修改时间等）

## 高级用法

### 批量处理文件

```python
from pyfile import FileOps

# 批量创建不同尾缀的文件
extensions = ['.txt', '.csv', '.json', '.xyz', '.myapp']
for i, ext in enumerate(extensions):
    FileOps.create_file(f"file_{i}{ext}", f"这是{ext}文件的内容")

# 列出所有文件
all_files = FileOps.list_files(".")
print(f"目录中的所有文件: {all_files}")

# 只列出特定尾缀的文件
txt_files = FileOps.list_files(".", "*.txt")
print(f"文本文件: {txt_files}")
```

### 获取文件信息

```python
from pyfile import FileOps

# 创建文件
FileOps.create_file("example.txt", "示例内容")

# 获取文件信息
info = FileOps.get_file_info("example.txt")
print(f"文件名: {info['name']}")
print(f"文件大小: {info['size']} 字节")
print(f"文件扩展名: {info['extension']}")
print(f"创建时间: {info['created']}")
print(f"修改时间: {info['modified']}")
```

### 安全文件操作

```python
from pyfile import FileOps

# 安全地创建嵌套目录结构
FileOps.create_file("deeply/nested/directory/config.cfg", "配置内容")

# 检查文件是否存在再操作
file_path = "important.data"
if FileOps.file_exists(file_path):
    content = FileOps.read_file(file_path)
    FileOps.copy_file(file_path, f"{file_path}.backup")
else:
    print("文件不存在，创建新文件")
    FileOps.create_file(file_path, "初始数据")
```

## API 参考

### FileOps 类

#### 创建文件
```python
FileOps.create_file(file_path: str, content: str = "") -> bool
```
创建指定路径的文件，支持任意尾缀。如果目录不存在会自动创建。

**参数**:
- `file_path`: 文件路径，可以包含任意尾缀
- `content`: 文件内容，默认为空

**返回**: 成功创建返回 True，否则返回 False

#### 读取文件
```python
FileOps.read_file(file_path: str) -> str
```
读取文件内容。

**参数**:
- `file_path`: 文件路径

**返回**: 文件内容字符串

#### 复制文件
```python
FileOps.copy_file(src: str, dst: str) -> bool
```
复制文件到指定位置。

**参数**:
- `src`: 源文件路径
- `dst`: 目标文件路径

**返回**: 成功复制返回 True，否则返回 False

#### 移动文件
```python
FileOps.move_file(src: str, dst: str) -> bool
```
移动文件到指定位置。

**参数**:
- `src`: 源文件路径
- `dst`: 目标文件路径

**返回**: 成功移动返回 True，否则返回 False

#### 删除文件
```python
FileOps.delete_file(file_path: str) -> bool
```
删除指定文件。

**参数**:
- `file_path`: 文件路径

**返回**: 成功删除返回 True，否则返回 False

#### 列出文件
```python
FileOps.list_files(directory: str, pattern: str = "*") -> List[str]
```
列出目录中匹配模式的文件。

**参数**:
- `directory`: 目录路径
- `pattern`: 文件匹配模式，默认为所有文件

**返回**: 文件路径列表

#### 创建目录
```python
FileOps.create_directory(directory_path: str) -> bool
```
创建指定目录。

**参数**:
- `directory_path`: 目录路径

**返回**: 成功创建返回 True，否则返回 False

#### 检查文件存在
```python
FileOps.file_exists(file_path: str) -> bool
```
检查文件是否存在。

**参数**:
- `file_path`: 文件路径

**返回**: 文件存在返回 True，否则返回 False

#### 获取文件信息
```python
FileOps.get_file_info(file_path: str) -> dict
```
获取文件的详细信息。

**参数**:
- `file_path`: 文件路径

**返回**: 包含文件信息的字典，包括名称、路径、大小、创建时间、修改时间和扩展名

## 项目结构

```
pyfile/
├── pyfile/           # 主包目录
│   ├── __init__.py  # 包初始化文件
│   └── core.py      # 核心功能实现
├── tests/           # 测试目录
│   ├── __init__.py
│   └── test_core.py # 核心功能测试
├── examples/        # 示例目录
│   └── example_usage.py  # 使用示例
├── LICENSE          # MIT 许可证
├── README.md        # 项目说明文档
├── requirements.txt # 项目依赖
└── setup.py         # 包安装配置
```

## 运行测试

确保已安装依赖后，运行测试套件：

```bash
python -m unittest discover tests
```

## 贡献指南

我们欢迎任何形式的贡献！请遵循以下步骤：

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 作者

Henry Liu - [2272424821@qq.com](mailto:2272424821@qq.com)

## 版本历史

- v0.1.0 (2025-8-30)
  - 初始版本发布
  - 包含基础文件操作功能
  - 支持创建任意尾缀文件

## 支持

如果您遇到任何问题或有任何建议，请通过以下方式联系：

- 创建 [Issue](https://github.com/Henry-code-Liu/pyfile/issues)
- 发送邮件至 [2272424821@qq.com](mailto:2272424821@qq.com)

## 常见问题

### Q: 如何处理大文件操作？
A: 当前版本适合处理中小型文件。对于大文件，建议使用分块读取/写入的方式，未来版本可能会添加对大文件的专门支持。

### Q: 是否支持异步操作？
A: 当前版本是同步操作。如果需要异步支持，可以考虑使用 `asyncio` 和 `aiofiles` 库结合使用。

### Q: 是否支持文件监控？
A: 当前版本不包含文件监控功能，但可以使用 `watchdog` 等库与 PyFile 结合使用。

---

⭐ 如果这个项目对您有帮助，请给它一个星标！
