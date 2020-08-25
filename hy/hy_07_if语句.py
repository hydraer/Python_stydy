# # 猜拳游戏
# import random
# computer = random.randint(0, 2)
# player = int(input("请输入剪刀（0）石头（1）布（2）"))
# # if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
# #     print('恭喜您赢了')
# # elif player == computer:
# #     print('平局，再来')
# # else:
# #     print('哎呀，输了，再来？')
# #     print('电脑出的是%i'%computer)
#
# print('you are win') if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1) else print('go on')

# 坐公交，有钱上车、有座坐下，没钱上不了车，且没座站着

print('公交车来了')
money = input('你有钱吗？"1为有，0为没有”')
if money == '1':
    print('土豪，请上车')
    seat = input('瞅瞅有座没，1为有，0为没有')
    if seat == "1":
        print('客官请坐')
    else:
        print('生命在于站立')
else:
    print('没钱坐什么公交车')