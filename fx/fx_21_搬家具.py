# 搬家具
class Fumiture():
    def __init__(self, area, name):
        self.area = 0
        self.name = ''


class Home():
    def __init__(self, address, area):
        self.address = address
        self.floor_area = area
        self.residual_area = 0
        self.fumiture_list = []

    def __str__(self):
        return f'您的房子在{self.address},占地面积{self.floor_area},剩余面积{self.residual},屋里家具有{self.fumiture_list}'

    def add_fumiture(self, area, name):
        self.residual_area = self.floor_area - area
        self.fumiture_list.append(name)


house = Home('北京', '100')

fumiture1 = Fumiture()
fumiture1.name = '双人床'
fumiture1.area = '8'
house.add_fumiture(fumiture1.area, fumiture1.name)
print(house)

fumiture2 = Fumiture('沙发', 18)

fumiture3 = Fumiture()
fumiture3.name = '足球场'
fumiture3.area = '1200'
