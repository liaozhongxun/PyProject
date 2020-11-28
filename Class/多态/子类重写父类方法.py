class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '正在睡觉')


class Student(Person):
    def __init__(self, name, age, school):
        # self.name = name
        # self.age = age
        # 部分重写:在父类的基础上添加自己功能两种方式
        #         1、父类名.方法名(self,参数列表), Person.__init__(self, name, age)
        #         2、使用super直接调用父类的方法
        super(Student, self).__init__(name, age)
        self.school = school

    def sleep(self):  # 完全重写父类方法
        print(self.name + '正在' + self.school + '睡觉')


s = Student('xm', 20, '注明大学')
s.sleep()
