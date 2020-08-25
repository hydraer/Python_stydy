# 石头剪刀布游戏
import random

input('猜拳游戏现在开始')
player = int(input('请出拳：0为剪刀；1为石头；2为布头'))
computer = random.randint(0, 2)
print(computer)
if player == 0:
    if computer == 0:
        print('电脑出的剪刀，平局了，再来一次')
    elif computer == 1:
        print('电脑出的石头，你输了')
    else:
        print('电脑出的布，恭喜你赢了')
elif player == 1:
    if computer == 0:
        print('电脑出的剪刀，恭喜你赢了')
    elif computer == 1:
        print('电脑出的石头，平局了，再来一次')
    else:
        print('电脑出的布头，你输了')
elif player == 2:
    if computer == 0:
        print('电脑出的剪刀，你输了')
    elif computer == 1:
        print('电脑出的石头，恭喜你赢了')
    else:
        print('电脑出的布头，平局了，再来一次')
else:
    print('只能出剪刀石头布哦，请按照提示输入')