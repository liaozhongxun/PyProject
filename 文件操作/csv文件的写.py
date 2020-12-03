# 以纯文本储存表格数据
'''
 文本文件中以一定格式写入数据,将文件后缀改成csv，就能在excel中正常打开
 tan1,tab2,tab3,tab4
 1val,2val,3val,4val
'''
import csv
file = open('testdemo.csv','w',encoding='utf8',newline='')
writ = csv.writer(file)
writ.writerow(['name','age','height'])
writ.writerow(['个','18','130'])
writ.writerow(['如','19','135'])

writ.writerows([
    ['t1','t2','t3','t4'],
    ['tv1','t2','t3','t4'],
    ['tv1','tv2','t3','t4'],
])
file.close()