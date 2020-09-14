class A():
    def __init__(self):
        self.num = 1
    def info_print(self):
        print(self.num)

class B(A):
    pass

b = B()

b.num = 2
b.info_print()

# 1、单继承之煎饼果子
class Master():
    def __init__(self):
        self.kongfu = '古法煎饼果子秘方'
    def make_cake(self):
        print(f'利用{self.kongfu}制作煎饼')

class Prentice(Master):
    pass

xiaoming = Prentice()

xiaoming.make_cake()

# 2、多继承
class School():
    def __init__(self):
        self.kongfu = '校级煎饼果子秘方'
        self.mifnag = '山东煎饼果子秘方'
    def make_cake(self):
        print(f'糊弄糊弄{self.mifnag}制作煎饼')
        # super().__init__()
        # super(School, self).make_cake()
    def make_bing(self):
        print(f'糊弄糊弄{self.mifnag}制作煎饼')

class Prentice1(School):
    def __init__(self):
        self.kongfu = '独创煎饼果子秘法'
        self.__money = 2000000
    def set__money(self, money):
        self.__money = money

    def get__money(self):
        return self.__money

    def __info_print(self):
        print(self.kongfu)
        print(self.__money)
    def make_self_bing(self):
        self.__init__()
        print(f'糊弄糊弄{self.kongfu}制作煎饼')
    def make_Master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
    def make_School_cake(self):
        School.__init__(self)
        School.make_cake(self)
    def make_old_cake(self):
        # super().__init__()
        # super().make_cake()
        super().make_cake()

xiaofei = Prentice1()

print(xiaofei.kongfu)
# print(xiaofei.mifnag)
# xiaofei.make_cake()
xiaofei.make_self_bing()
xiaofei.make_School_cake()
xiaofei.make_Master_cake()
xiaofei.make_old_cake()

print(xiaofei.get__money())
xiaofei.set__money(111)
print(xiaofei.get__money())
print(xiaofei.get__money())