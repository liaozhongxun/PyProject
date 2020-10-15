import uuid

print(uuid.uuid1()) #基于MAC地址、时间戳、随机数生成
'''
生成一个长度为36除横杆外32个字符的十六进制字符串
可能生成的个数有16**32种,重复的概率是16**32分之一
'''

print(uuid.uuid3(uuid.NAMESPACE_DNS,'abc'))  #基于算法与给定字符串生成固定uuid
print(uuid.uuid5(uuid.NAMESPACE_DNS,'abc'))  #基于算法与给定字符串生成固定uuid
print(uuid.uuid4())  #随机生成,常用,速度比uuid1快但重复率存在