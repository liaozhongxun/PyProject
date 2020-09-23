str = "helloabcdeddd"
print(len(str))

print('你'.encode('gbk'))
print('你'.encode('utf8'))
print('你'.encode())

x=b'\xc4\xe3'
print(x.decode('gbk'))

print('x9' in 'xpp')

