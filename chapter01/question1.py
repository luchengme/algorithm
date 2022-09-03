# 求两个自然数m和n的最大公约数
# ⑴ 至少设计出三个版本的求最大公约数算法，用伪代码描述各个算法；
# ⑵ 对所设计的算法采用大O符号进行时间复杂性分析；


# 欧几里得算法
# 定理：两个整数的最大公约数等于其中较小的那个数和两数相除余数的最大公约数
# 时间复杂度O(log n)
def f1(a, b):
    mod = a % b
    while mod != 0:
        a = b
        b = mod
        mod = a % b
    return b


# 暴力循环求解
# 时间复杂度O(n)
def f2(a, b):
    s = a if a < b else b
    while s > 0:
        if a % s == 0 and b % s == 0:
            return s
        s -= 1


# 更相减损术
# 1、先判断两个数的大小，如果两数相等，则这个数本身就是就是它们的最大公约数。
# 2、如果不相等，则用大数减去小数，然后用这个较小数与它们相减的结果相比较，如果相等，则这个差就是它们的最大公约数，而如果不相等，则继续执行操作2。
# 时间复杂度O(n)
def f3(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


# from random import randint
#
# res1 = []
# res2 = []
# res3 = []
# for i in range(1000):
#     a = randint(1, 1000)
#     b = randint(1, 1000)
#     res1.append(f1(a, b))
#     res2.append(f2(a, b))
#     res3.append(f3(a, b))
#
# print(res1 == res2 == res3)

