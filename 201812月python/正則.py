#
import re
tels=["13100001234","18912344321","10086","18800007777",'13177036948','13177036947']

for tel in tels:
    com = re.compile('1\d{9}[0-3,5-6,8-9]$')
    res = com.match(tel)   
    if res:
        print('{}:OK'.format(res.group()))
    else:
        print('{}:NG'.format(tel))
