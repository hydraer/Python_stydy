# 学员管理系统
from StudentManagerSystem import student
class managerSystem():
    def __init__(self):
        self.students = []
    def run(self):
        '''
        功能界面
        :return:
        '''
        self.load_student()
        while True:
            self.show_menu()
            i = input('请输入您要选择的功能')
            if i == '1':
                self.add_student()
            elif i == '2':
                self.del_student()
            elif i == '3':
                self.modify_student()
            elif i == '4':
                self.serch_student()
            elif i == '5':
                self.show_student()
            elif i == '6':
                self.save_student()
            elif i == '7':
                break
            else:
                print('请输入正确选项')
        pass
    def show_menu(self):
        '''
        显示菜单
        :return:
        '''
        print('*' * 10, end='')
        print('欢迎进入学员管理系统', end='')
        print('*' * 10)
        print('1、添加学员')
        print('2、删除学员')
        print('3、修改学员信息')
        print('4、查找学员')
        print('5、保存所有信息')
        print('6、显示所有学员信息')
        print('7、退出系统')
    def add_student(self):
        '''
        增加学员
        :return:
        '''
        print('添加学员')
    def del_student(self):
        '''
        删除学员
        :return:
        '''
        pass
    def modify_student(self):
        '''
        修改学员
        :return:
        '''
        pass
    def serch_student(self):
        '''
        查找学员
        :return:
        '''
        pass
    def save_student(self):
        '''
        保存学员信息
        :return:
        '''
        pass
    def load_student(self):
        '''
        加载学员信息
        :return:
        '''
        pass
    def show_student(self):
        '''
        显示所有学员信息
        :return:
        '''
        pass

if __name__ == '__main__':
    managerSystem1 = managerSystem()
    managerSystem1.run()