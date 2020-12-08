import json

'''
序列化数据
json本质就是一个字符串,里面是双引号的字符串，转json，元素类型对应js类型
作用：
    1、序列化数据（dump,dumps），使数据转字符串，可以在文件操作是写入文件中，
    2、反序列化数据（load,loads），使字符串转数据

'''
list = ["name", 'age']

file = open('jsondump.txt', 'w', encoding='utf8')

liststr = json.dumps(list)  # 转字符串,不会保留数据到文件里
liststr2 = json.dump(list, file)  # 转字符串,并且保留数据到指定文件里

file.close()

# =====================================================

file1 = open('jsondump.txt', 'r', encoding='utf8')

strs = '["aaa","bbb"]'
strsloads = json.loads(strs)
strsload = json.load(file1)  # 读出文件中的json数据并反序列化为可用数据
print(type(strsloads))
print(strsload)

file1.close()
