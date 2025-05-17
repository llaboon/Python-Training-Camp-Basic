"""
练习: HTTP请求

描述：
本练习帮助您学习如何使用requests库发送HTTP请求并处理响应。
注意：运行此练习前，请确保已安装requests库（pip install requests）。

请补全下面的函数，实现发送HTTP请求并处理响应的功能。
"""
import requests
import json
def get_website_content(url):
    """
    发送GET请求获取网页内容
    
    参数:
    - url: 目标网站URL
    
    返回:
    - 包含响应信息的字典: 
      {
        'status_code': HTTP状态码,
        'content': 响应内容文本,
        'headers': 响应头部信息
      }
    """
    # 请在下方编写代码
    # 使用requests.get()发送GET请求
    # 返回包含状态码、内容和头部信息的字典
    response=requests.get(url)
    return {
        'status_code': response.status_code,
        'content': response.text,  # 使用response.text获取字符串内容
        'headers': dict(response.headers)
    }
    #return {'status_code':r.status_code,'content':json.loads(r.content),'headers':r.headers}
    pass

def post_data(url, data):
    """
    发送POST请求提交数据
    
    参数:
    - url: 目标网站URL
    - data: 要提交的数据字典
    
    返回:
    - 包含响应信息的字典:
      {
        'status_code': HTTP状态码,
        'response_json': 响应的JSON数据(如果有),
        'success': 请求是否成功(状态码为2xx)
      }
    """
    # 请在下方编写代码
    # 使用requests.post()发送POST请求
    # 返回包含状态码、响应JSON和成功标志的字典
    response = requests.post(url, json=data)

    # 解析JSON响应（如果有）
    try:
        response_json = response.json()
    except ValueError:
        response_json = None

    # 返回响应信息
    return {
        'status_code': response.status_code,
        'response_json': response_json,
        'success': response.ok  # 状态码为2xx时返回True
    }
    r=requests.post(url,data)
    return {'status_code':r.status_code,'response_json':json.loads(r.content),'success':r.status_code<300&r.status_code>=200}
    pass 