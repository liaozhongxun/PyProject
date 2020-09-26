dicts = {'a':1,'b':2,'c':3,'e':5,'d':4}
dicts2 ={'f':6}

print(dicts['a'])


print(dicts.update(dicts2))
print(dicts)
print(dicts2)




lists = ['c','g','r','t','t','w','a','w','t','b','b','a','t']
counts ={}
for i in lists:
    if counts.get(i) == None:
        counts[i] = lists.count(i)

print(counts)

#输入用户名 如果已存在提示用户,否则继续输入年龄 以字典形式展示出来
userInfo =[]
while True:
    username = input("请输入姓名:")

    if username =='Exit':
        break

    for ui in userInfo:
        if ui['name'] == username:
            print('该用户名已存在')
            break
    else:
        userage = input('请输入年龄:')
        userInfo.append({'name': username, 'age': userage})

    print(userInfo)




