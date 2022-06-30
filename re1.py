# 王宇鑫创建的学习代码

import re

mac = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

a = 'VLAN ID'
b = 'MAC'
c = 'Type'
d = 'Interface'

e = re.match('(\d{1,3})\s+([0-9a-z]+\.[0-9a-z]+\.[0-9a-z]+)\s+(\w+)\s+([A-Z]\w\d/\d+/\d+)',mac).groups()

print(f'{a:<10s}: {e[0]}')
print(f'{b:<10s}: {e[1]}')
print(f'{c:<10s}: {e[2]}')
print(f'{d:<10s}: {e[3]}')
