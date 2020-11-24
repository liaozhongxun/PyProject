class Singleton:
    instance = None
    is_first = True

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            # 申请内存,创建对象,并把对象的类型设置成cls
            cls.instance = object.__new__(cls)
        return cls.instance

    def __init__(self, a, b):
        if self.is_first:  # 第一次是类属性is_first是后面的无法更改第一次的属性
            self.a = a
            self.b = b
            self.is_first = False  # 实例属性is_first


'''
1、调__new__方法申请内存
2、如果不重写__new__方法,每次都会调用object的__new__方法，并申请内存
3、__new__重写，可以随意控制要不要生气新内存
'''

s1 = Singleton('11', '22')
s2 = Singleton('33', '44')

print(s1 is s2)  # 因为所有实例指向同一个地址，创建再多实例操作都是一个
