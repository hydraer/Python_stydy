# 烤羊肉串
class cook_mutton():
    def __init__(self):
        self.cook_time = 0
        self.cook_static = '生的'
        self.condiments = []
    def __str__(self):
        return f'羊肉串烤了{self.cook_time}分钟，{self.cook_static},放了{self.condiments}'
    def __del__(self):
        print('羊肉串没了')
    def cook(self, time):
        self.cook_time = time
        if 0 <= time < 2:
            self.cook_static = '羊肉串变色了'
        elif 2 <= time < 4:
            self.cook_static = '羊肉串快熟了'
        elif 4 <= time < 6:
            self.cook_static = '羊肉串儿正嫩呢，可以吃了'
        elif 6 <= time < 8:
            self.cook_static = '羊肉串快老了，赶紧吃'
        elif time >= 8:
            self.cook_static = '羊肉串烤糊了，扔了吧'
    def add_condiments(self, condiment):
        self.condiments.append(condiment)

mutton = cook_mutton()
mutton.cook(1)
print(mutton)

mutton.cook(3)
mutton.add_condiments('盐')
print(mutton)

mutton.cook(5)
mutton.add_condiments('孜然')
print(mutton)

mutton.cook(7)
mutton.add_condiments('辣椒面')
print(mutton)

mutton.cook(9)
print(mutton)

del mutton
