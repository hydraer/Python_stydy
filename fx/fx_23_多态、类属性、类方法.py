# 1、多态
class Dog():
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        print(cls.__tooth)
    def work(self):
        print('指哪儿打哪儿')
    def __init__(self):
        self.tail = 1
    def info_print(self):
        print(self.tail)
    @staticmethod
    def print_info():
        print('这是一个狗狗类，用于创建狗狗')


class ArmyDog(Dog):
    def work(self):
        print('捉拿犯人')

class DrugDog(Dog):
    tooth = 22
    def __init__(self):
        self.tail = 2
    def work(self):
        print('追踪毒品')
    def info_print(self):
        print(self.tail)

class Person(object):
    def word_with_dog(self, b):
        b.work()#自动匹配方法？

# xiaofei = Person()
# dog1 = DrugDog()
# dog2 = ArmyDog()
# dog3 = Dog()
# xiaofei.word_with_dog(dog1)
# xiaofei.word_with_dog(dog2)
# xiaofei.word_with_dog(dog3)

# 2、类属性、类属性修改、类属性与实例属性区别
Dog.get_tooth()
# Dog.tooth = 12
# dog = Dog()
# dog.tooth = 11
# print(dog3.tooth)
# dog.info_print()
# dog2.info_print()
# print(ArmyDog.tooth)
# dog3.info_print()
Dog.print_info()
dog = Dog()
dog.print_info()