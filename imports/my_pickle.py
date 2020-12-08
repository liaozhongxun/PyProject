# pickle 将Python中任意对象转成二进制，包括自定义，

import pickle
'''
序列化数据
pickle本质就是一个二进制
    1、序列化数据（dump,dumps），使数据转二进制
    2、反序列化数据（load,loads），使二进制转数据

用法与json模块一样，rb与wb ，但应用场景不一样
'''

'''
    pickle与json的区别
    pickl将数据原封不动转为二进制，包括对象的属性和方法，但是这个二进制只能在Python识别
    json只能保存一部分信息（基本数据类型），主要用来在不同平台传递数据
    
'''

