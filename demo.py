print("hello word")

a = {'a','b','c'}
b = {'a':1,'b':2}
c = (1,2,3)
d =[1,'2']
print(type(a),type(b),type(c),type(d))

e ='12'
print(int(e))

print(5>1)

print(5 or 8)

age = 18

if age<18:
    print('小于18')
elif age==18:
    print("等于18")
else:
    print('大于18')

print(5 if 8>4 else 6)

whiledate = 0
while whiledate < 10:
    print('满足条件 执行代码')
    whiledate+=1

#range 内置类用来生成指定区间的整数序列
for forx in range(1,10): # in后面必须是可迭代对象如:字符串 列表 字典 元祖 集合 range 等
    print(forx)

