# 王宇鑫创建的学习代码
# 补齐被删除的代码
department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_PEES_SEC = 456789.12456
COURSE_PEES_Python = 1234.3456

line1 = 'department1 name:%-12s Manager:%-12s COURSE_PEES:%-12.2f The end!' % (department1,depart1_m,COURSE_PEES_SEC)
line2 = 'department2 name:%-12s Manager:%-12s COURSE_PEES:%-12.2f The end!' % (department2,depart2_m,COURSE_PEES_Python)

#line1 ='department1 name:{:<12s}Manager:{:<12s}COURSE_PEES:{:<12.2f}The end!'.format(department1,depart1_m,COURSE_PEES_SEC)
#line2 ='department2 name:{:<12s}Manager:{:<12s}COURSE_PEES:{:<12.2f}The end!'.format(department2,depart2_m,COURSE_PEES_Python)

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)

