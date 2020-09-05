# 数字以内累加和
def sum_numbers(num):
    if num == 1:
        return 1
    return sum_numbers(num) + sum_numbers(num - 1)

print(sum_numbers(5))