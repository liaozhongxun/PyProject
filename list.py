from functools import reduce

lists = [100,1001,100]

numbs = lists
lists = [100,1001,444]
print(numbs)
print(lists)

lists2 = [1]
print(lists + lists2)
print(lists)
print(lists2)

listsSort = [
    {'age':28,'count':50,'name':'aaa'},
    {'age':70,'count':20,'name':'bbb'},
    {'age':90,'count':59,'name':'ccc'},
    {'age':17,'count':70,'name':'ddd'},
    {'age':13,'count':93,'name':'eee'},
]

# def callbacks(item):
#     return item['age'] #指定一个可以比较的值
#
# listsSort.sort(key=callbacks)

listsSort.sort(key=lambda item:item['age'])

print(listsSort)



print(list(filter(lambda item: item['age'] > 25, listsSort)))


def mapCallback(item):
    item['age'] += 1
    return item


print(list(map(mapCallback , listsSort)))


def reduceCount(x,y):
    return x+y['age']
print(reduce(reduceCount,listsSort,0)) #callback,可迭代对象,默认值   如果没有默认值从第0,1开始算,否则从默认,0开始算

print(abs(-4))