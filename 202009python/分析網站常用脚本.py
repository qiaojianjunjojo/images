# coding = utf-8
'''
usage: repalce the url with yours and run it.
'''
import re
import requests

url = 'http://10.189.127.62:40023/mod-portal/'
response = requests.get(url) 
response.encoding = 'utf-8-sig'  
texts = re.split(r'[\n]',response.text) #通過換行符將很長的一段html切成小段
l = set() # 定定義一個不重複的集合
pattern = r'<([a-zA-Z].*?\s*?)>'  # 匹配型如<meta xxxxx>, <script xxxx>

for text in texts:
    r = re.findall(pattern,text) 
    for item in r:
        l.add(item.split(' ')[0])
print(f'url:{response.url}\n常用標簽：{l}\n數量：{len(l)}')