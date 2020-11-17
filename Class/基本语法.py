class Student:
    #这个属性直接定义在类里,是一个元组,用来规定对象可以存在的属性
    __slots__ = ('name','height','age','props')

    def __init__(self,name,height,age):
        self.name = name
        self.height = height
        self.age = age

    def run(self):
        print('正在跑步')

    def eat(self):
        print('正在吃东西')

    '''
    魔法方法 类里特殊的一些方法
        不需要手动调用，在合适时机自动调用, 格式 __xxx__
        可以直接调用 s1.__repr__()
        方法名都是系统规定好的,合适时机才会自动调用
            如:
            __init__(): 在创建对象时自动调用
            __del__(self): 对象销毁时自动调用 如程序运行完或del s1就能触发
            __str__(self): || __repr__(self): 打印对象s1 的时候默认调用这个,返回一个地址,__str__优先级高
            __call__(self,*args,**kwargs): 当对象被当做函数调用是触发  s1()
            __eq__(self,other):   self 等号左边, other 等号右边
            __ne__  不等于时调用
            __gt__  大于时调用
            __setattr__  将对象当字典设置值自动调用
            str('str'),int('1')等类型转换方法,也会分别调用__str__ __int__
            。。。
            
    '''

    def __str__(self):
        return "姓名:{},年龄:{}".format(self.name,self.age)

    def __repr__(self):
        return "repr"



# Student() 会自动调用类的 __init__方法
# 使用Student创建了两个实力对象 s1和s2
# 两个实例都有name,age,height属性和 run与eat方法
s1 =Student('小米','1.78',18)
s2 =Student('小丽','2.78',18)

s1.run()
print(s1)

# is判断是否为同一个内存 False
print(s1 is s2)

# == 调用对象__eq__()

# 默认 是s1.paops  如果属性不存在会自动添加，称动态属性
s1.props = "props"

#查看所有方法和属性包括自己定义的和内置的
print(dir(s1))
print(s1.__class__) #类名
print(s1.__dir__)
print(s1.__doc__)
print(s1.__module__)

'''
Student('小丽','2.78',18) 过程如图一   
1、调用 __new__方法 申请一段内存空间
2、调用 __init__方法传入参数,并将self指向申请好的内存空间
3、变量 s2也指向申请好的内存空间
'''
