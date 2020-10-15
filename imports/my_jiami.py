import hashlib
import hmac

# 两个都是加密模块
# hashlib 主要支持 md5 和 sha 加密

# md5加密  需要将加密的内容转换为二进制
hsmd5 = hashlib.md5()  # 生成md5对象
hsmd5.update('abc'.encode('utf-8'))
print(hsmd5.hexdigest())
# 可以不需要update
hsmd52 = hashlib.md5('abc'.encode('utf-8'))  # 生成md5对象
print(hsmd52.hexdigest())

# hsa系列 sha1/sha224/sha256/sha384 生成方法与md5一样
# 224代表224位生成十六进制的字符个数  4bit为一个十六进制字符

# hmac加密可以指定秘钥
h = hmac.new('h4'.encode(),'你好'.encode())  #用'h'对'你好'进行加密
print(h.hexdigest())
'''
加密方式
    单项加密 -> md5/sha -> 只有加密（明文-密文）过程,没有解密过程
        网上的一些解密都是只能解一些基础的,在其数据库储存的少量字符
        文件的md5/sha码作用:下载文件之前，官方将文件生成一个md5/sha码,等下载完成之后用户将下载到的文件转md5/sha与官方进行对比
        如果不一样说明下载过程中文件被篡改了
    对称加密
'''
