# 以纯文本储存表格数据
'''
 文本文件中以一定格式写入数据,将文件后缀改成csv，就能在excel中正常打开
 tan1,tab2,tab3,tab4
 1val,2val,3val,4val
'''
import csv
file = open('testdemo.csv','r',encoding='utf8',newline='')
r = csv.reader(file)
for data in r:
    print(data)

file.close()