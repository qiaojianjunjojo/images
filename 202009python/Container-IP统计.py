#coding = utf-8
'''
usage:将需要统计的log复制到log.txt，运行该脚本文件；或者指定log文件所在的path；

用正则表达式将log中每行中的IP 匹配出来；
'''
import re
with open('log.txt','r',encoding='utf-8') as file:
    str = file.readlines()
    str_del_enter = [x.strip('\n') for x in str]  
    pattern = re.compile(r'^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
    str_legal_ip = [pattern.search(x).group() for x in str_del_enter if pattern.search(x)] 
    print(f"总访问次数：{len(str_legal_ip)}")
    print(f"IP总数为：{len(set(str_legal_ip))}")
    print("明细列表：")
    for i in set(str_legal_ip):
        print(i,end = '||')


