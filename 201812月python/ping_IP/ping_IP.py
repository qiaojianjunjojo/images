#coding = utf-8
'''
2020/4/8 批量ping ip地址，將能ping通跟不能ping通的存放在不同的記事本
writen by qjj
usage:將要ping的ip 放在host.txt中，一行一個ip
'''



import time,os
start_Time=int(time.time()) #记录开始时间
def ping_Test():
    ips=open('host.txt','r')
    ip_True = open('ip_True.txt','w')
    ip_False = open('ip_False.txt','w')
    count_True,count_False=0,0
    for ip in ips.readlines():
        ip = ip.replace('\n','')
        return1=os.system('ping -n 4 -w 5 %s'%ip)
        if return1:
            print('ping %s is fail'%ip)
            ip_False.write(ip + '\n')
            count_False += 1
        else:
            print('ping %s is ok'%ip)
            ip_True.write(ip + '\n')
            count_True+=1
    ip_True.close()
    ip_False.close()
    ips.close()
    end_Time = int(time.time())
    print("time(秒)：",end_Time - start_Time,"s")#打印并计算用的时间
    print("ping通数：",count_True,"   ping不通的ip数：",count_False)

ping_Test()
