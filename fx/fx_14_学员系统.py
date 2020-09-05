# 系统简介
# 1、添加学员
# 2、删除学员
# 3、修改信息
# 4、查看学员信息
# 5、查看所有学员信息
# 6、退出系统
# 声明学生集合
students = [{'name':'Lilei', 'age':'22', 'tel_num':'212112'}]
flag = True;

# 打印功能页面
def print_info():
    global students
    print('*' * 20)
    print('欢迎进入学员管理系统')
    print('1、添加学员')
    print('2、删除学员')
    print('3、查看学员信息')
    print('4、修改学员信息')
    print('5、查看所有学员信息')
    print('6、退出系统')
    print('*' * 20)

# 定义各个方法
def stu_add():
    '''
    添加学员信息
    :return:
    '''

    global students
    student_name = input('请输入学员姓名')
    for i in students:
        if student_name == i['name']:
            print('该学员已存在')
            return
    student = {}
    student_age = input('请输入学生年龄')
    student_tel_num = input('请输入学生手机号')
    student['name'] = student_name
    student['age'] = student_age
    student['phont'] = student_tel_num

    students.append(student)
    print('学员信息添加成功')
def stu_del():
    '''
    删除学员信息
    :return:
    '''
    student_name = input('请输入学员姓名')
    for i in students:
        if i['name'] == student_name:
            del i
            print('该学员信息已删除')
            return
    print('查无此人，请核对您的输入信息')

def stu_change():
    '''
    修改学员信息
    :return:
    '''
    student_name = input('请输入学员姓名')
    for i in students:
        if i['name'] == student_name:
            i['phone'] = input('请输入修改后的手机号')
            i['age'] = input('请输入修改后的年龄')
            print('学员信息修改成功')
            return
    print('查无此人，请核对您的输入信息')
def stu_seek():
    '''
    根据姓名查找学员信息
    :return:
    '''
    student_name = input('请输入您要查询的学员你姓名')
    global students
    for i in students:
        if student_name == i['name']:
            print(f'您所查询的学员信息为{i}')
            return
    print('查无此人，请核对您的输入信息')
def stu_all():
    '''
    输出所有学员信息
    :return:
    '''
    print(students)
def stu_exit():
    '''
    退出系统
    :return:
    '''
    global flag
    flag = False
    print('退出系统')

while flag:
    print_info()
    user_num = input('请输入选项')
    if user_num == '1':
        stu_add()
    elif user_num == '2':
        stu_del()
    elif user_num == '3':
        stu_seek()
    elif user_num == '4':
        stu_change()
    elif user_num == '5':
        stu_all()
    elif user_num == '6':
        stu_exit()
    else:
        print('输入错误，请重新输入')
