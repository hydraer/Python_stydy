# 函数提高
# 位置参数、关键字参数、缺省参数、不定长位置参数、不定长关键字参数
def circle(father, mother, *args, grandpa, grandma, wife='null', **ps):
    print(f'我的爸爸是{father}，我的妈妈是{mother}，我的爷爷是{grandpa},我的奶奶是{grandma},妻子是{wife}，{args},{ps}')

circle('Kun', 'Ning',                   # 位置参数
       'girl', 'lover', 'peace',        # 不定长位置参数
       sex = 'boy', like = 'girl',      # 不定长关键字参数
       grandma= 'Peng',  grandpa= 'Wen' # 关键字参数
       )


tuple1 = (1, 2)
num1, num2 = tuple1
print(num1)
print(num2)

# 引用
print('引用')
def test1(a):
    print('引用改变')
    print(a)
    print(id(a))
    a += a
    print(a)
    print(id(a))

b = 100
test1(b)

c = [1, 2]
test1(c)

list1 = {'c': 1,'b': 2}
print(f'list1的ID：{id(list1)}')
print(f'list1[1]的ID:{list1['c']}')