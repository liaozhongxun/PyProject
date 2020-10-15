import random

print(random.randint(2, 9))  # 生成[2,9]的随机整数
print(random.randrange(2, 9))  # 生成[2,9)的随机整数
print(random.random())  # 生成[0,1)的随机浮点数

print(random.choice([1, 7, 9])) #在可迭代对象里随机抽取1个元素

print(random.choices([1, 7, 9,7])) #在可迭代对象里随机抽取1个元素,生成一个列表

print(random.sample([1, 7, 9],2)) #在可迭代对象里随机抽取n个元素
