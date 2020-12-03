# open(file,mode,encoding),文件路径,文件模式[r只读][w写][b以二进制形式读写，配合r或w],编码方式
# 拿到一个TextIOWrapper，可以对TextIOWrapper进行操作
# window系统默认gbk打开文件,确保打开的编码与操作文件的编码一致
# 路径使用从右到左的斜杠/,Windows复制的文件路径是反斜杠\,虽然会认识但是会被当做转意符号

file = open('test.txt', 'r', encoding='utf8')
# r模式
print(file.read())  # 默认读取所有，文件不存在会报错
file.seek(0, 0)
print(file.read(10))  # read加参数 每次读取 指定读取长度，不然读取大文件很耗cpu与内存
file.seek(0, 0)
print(file.readline())  # 只读取一行
file.seek(0, 0)
print(file.readline())  # 将所有行读取,并放在一个列表里

# print(file.write('写入并覆盖原有内容,文件不存在就新增文件'))

file.close()  # 操作完之后 记得关闭

'''
模式：
    r:读
    w:写
    t:文本形式打开
    a:追加内容
    rb:二进制形式读
    wb:二进制形式写(二进制操作就不能有编码了)
    
    r+:可读基础上添加可写(少)
    w+:可写基础上添加可读(与r+区别文件不存在不会报错)(少)
'''
# file.seek(0,0);可读可写的情况下写入文字光标停在最后,就读不到前面的内容了，seek将关闭定到指定位置
