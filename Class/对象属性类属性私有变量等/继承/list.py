class Animal(object):  # 继承自object，不指定默认使用object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '正在睡觉1')


class Animal2(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '正在睡觉2')


class Dog(Animal):  # 继承自Animal
    def bark(self):
        print(self.name + '正在叫')


class Student(Animal, Animal2):  # 多继承
    def study(self):
        print(self.name + '正在学习')


# 子类没有的方法会自动去父类查找，知道object
# 父类的属性和方法子类可以直接使用
stu = Student('xuesheng', 10)
dog = Dog('dog', 3)
stu.sleep()
stu.study()
dog.sleep()

# 注意事项

# 查看多继承时调用父类方法的优先级,深度优先
print(Student.__mro__)
