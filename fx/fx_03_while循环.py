
row = 1
while row < 10:
    line = 1
    while line <= row:
        print(f'{line} * {row} = {row * line}', end= '\t')

        line = line +1
    else:
        print()
    row += 1
else:
    print('九九乘法表')