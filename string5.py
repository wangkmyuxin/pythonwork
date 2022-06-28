# 王宇鑫创建的学习代码
#RE匹配IP地址，并格式化打印结果

import re

str1 = 'Port-channel1.189   192.168.189.254   YES  CONFIG   up'
str2 = re.match('(\w+-\w+\d+\.\d+)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+\s+(\w+)',str1).groups()

print('-'*30)
print('{:<8}：{:<20}'.format('接口',str2[0]))
print('{:<8}：{:<20}'.format('IP地址',str2[1]))
print('{:<8}：{:<20}'.format('状态',str2[2]))
