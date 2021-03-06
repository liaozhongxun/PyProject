class Person(object):
    type = '人类'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 1000  # 以连个下划线开头的变量 私有变量

    def __demo(self):
        print("以下划线开头的函数 私有函数,外面无法调用")

    def get_money(self):
        #  xxxxx操作
        return self.__money

    # 普通对象方法实例对象和 Person都能调用
    # 普通对象方法有一个self指的是实例对象
    def eat(self, name):
        print('调用了Eat方法' + name)

    # 如果方法里面没有用的任何实例属性，可以将它设置成static
    @staticmethod
    def demo():
        print('调用了demo静态方法方法')

    # 如果方法里面只用到类属性可以定义成类方法
    # 参数cls(类对象)会自动传参,不需要手动传
    #
    @classmethod
    def classdemo(cls):
        print(cls.type)


# p1是通过Person创建出来的实例对象
p1 = Person('张三', '20')
p2 = Person('李四', '20')

'''
1、 p1、p2实例对象
    只有创建了实例对象,这个对象就有name和age属性
    对象属性是每个对象都单独保存的属性，实例间互不影响
    对象属性是__init__里定义的属性

2、 Person 类对象
    类属性是定义在类里,函数外的属性,只有一份
    类属性可以通过类对象(Person.type)和实例对象(p1.type)获取
    类属性只能通过类对象修改,实例对象无法修改(实例对象会在对象属性中新增)  

3、私有属性
    以下划线开头
    外部获取: p1._Person__money  一般不建议外面用
            通过函数操作私有属性
    内部正常使用
    def __demo(self) 使用函数外面也不能直接调用
    
'''

print(Person.type)
print(p1.type)

print(p1._Person__money)
print(p1.get_money())

# p1调用不需要传self,会字动将p1对象传到self
p1.eat('p1')

# 这种不会自动传self需要手动指定self
Person.eat(p1, 'p1')

# 静态方法调用，可以不用传实例对象，直接通过类名调用静态方法
p1.demo()
Person.demo()

# 调用类方法
Person.classdemo()
p1.classdemo()
