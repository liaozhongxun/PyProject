class Student:
    def __init__(self,name,height,age):
        self.name = name
        self.height = height
        self.age = age

    def run(self):
        print('正在跑步')

    def eat(self):
        print('正在吃东西')

# Student() 会自动调用类的 __init__方法
# 使用Student创建了两个实力对象 s1和s2
# 两个实例都有name,age,height属性和 run与eat方法
s1 =Student('小米','1.78',18)
s2 =Student('小丽','2.78',18)
s1.run()


'''
Student('小丽','2.78',18) 过程如图一   
1、调用 __new__方法 申请一段内存空间
2、调用 __init__方法传入参数,并将self指向申请好的内存空间
3、变量 s1、s2也指向申请好的内存空间
'''
