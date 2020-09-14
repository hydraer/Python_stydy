# 学员类：包含姓名、性别、手机号
class Student():
    def __init__(self, name, sex, tel):
        self.name = name
        self.sex = sex
        self.tel = tel

    def __str__(self):
        print(f'学员姓名：{self.name},学员性别：{self.sex},学员电话：{self.tel}')

