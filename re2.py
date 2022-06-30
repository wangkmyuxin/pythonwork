# 王宇鑫创建的学习代码
import re

show_conn = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

str1 = re.match('(\w+)\s+\w+\s+(\d+\.\d+\.\d+\.\d+:\d+)\s+\w+\s+(\d+\.\d+\.\d+\.\d+:\d+).*' \
                '(\d+:\d+:\d+).*\w+\s+(\d+).*\w+\s+(\w+)',show_conn).groups()
a = 'protocol'
b = 'server'
c = 'localserver'
d = 'idle'
e = 'bytes'
f = 'flags'
str2 = str1[3].split(':')
str3 = str2[0]+' 小时 '+str2[1]+' 分钟 '+str2[2]+' 秒'

print(f'{a:<13s} : {str1[0]}')
print(f'{b:<13s} : {str1[1]}')
print(f'{c:<13s} : {str1[2]}')
print(f'{d:<13s} : {str3}')
print(f'{e:<13s} : {str1[4]}')
print(f'{f:<13s} : {str1[5]}')
