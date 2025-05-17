"""
练习: 文件处理

描述：
本练习帮助您学习如何在Python中进行文件的读取和写入操作。

请补全下面的函数，实现文件的读取和写入功能。
"""
import tempfile
import os
def read_file(file_path):
    """
    读取文本文件内容
    
    参数:
    - file_path: 文件路径
    
    返回:
    - 文件内容字符串
    """
    # 请在下方编写代码
    # 使用open()函数打开文件并读取内容

    f=open(file_path,'r',encoding='utf-8')
    ret=f.read()
    f.close()
    print(ret)
    return str(ret)
    pass

def write_file(file_path, content):
    """
    写入内容到文本文件
    
    参数:
    - file_path: 文件路径
    - content: 要写入的内容
    
    返回:
    - 是否写入成功的布尔值
    """
    # 请在下方编写代码
    # 使用with语句和open()函数写入内容到文件
    f=open(file_path,"w",encoding='utf-8')
    f.write(content)
    f.close()
    return True
    pass


fd, temp_path = tempfile.mkstemp(text=True)
os.close(fd)

# 使用UTF-8编码写入内容
with open(temp_path, 'w', encoding='utf-8') as f:
    f.write("这是一个测试文件内容\n第二行内容")

try:
    # 测试读取文件
    content = read_file(temp_path)

    # 验证内容
    assert isinstance(content, str), "返回值应该是字符串"
    assert "这是一个测试文件内容" in content, "返回的内容应该包含原始文件内容"
    assert "第二行内容" in content, "返回的内容应该包含原始文件内容"
finally:
    # 删除临时文件
    try:
        os.unlink(temp_path)
    except:
        pass  # 忽略删除失败的错误