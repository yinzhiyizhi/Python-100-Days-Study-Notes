# 练习

import os
import time
import random

# 练习1：在屏幕上显示跑马灯文字。

def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


# 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。

def generate_code(code_len = 4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


# 练习3：设计一个函数返回给定文件名的后缀名。

def get_suffix(filename, has_dot = False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


# 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。

def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


# 练习5：计算指定的年月日是这一年的第几天。

def is_leap_year(year):
    """
    判断是否闰年
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year, month, date):
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


# 练习6：打印杨辉三角。

def triangles():
    L = [1]
    S = []
    while True:
        yield L
        L = [1] + S + [1]
        S = []
        for i in range(len(L) - 1):
            S.append(L[i] + L[i + 1])


# 综合案例2：约瑟夫环问题。
"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""

def main():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                counter += 1
                persons[index] = False
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')
