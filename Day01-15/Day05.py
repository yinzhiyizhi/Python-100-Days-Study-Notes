import math
from random import randint

"""
寻找“水仙花数”

水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）
三位的水仙花数共有4个：153，370，371，407
"""

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low**3 + mid**3 + high**3:
        print(num)


"""
寻找“完美数”
找出1~9999之间的所有完美数

完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
如果一个数恰好等于它的因子之和，则称该数为“完全数”。第一个完全数是6，它有约数1、2、3、6，除去它本身6外，其余3个数相加，1+2+3=6。
第二个完全数是28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。
第三个完全数是496，有约数1、2、4、8、16、31、62、124、248、496，除去其本身496外，其余9个数相加，1+2+4+8+16+31+62+124+248=496。
后面的完全数还有8128、33550336等等。
"""

for num in range(1, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)


"""
“百钱百鸡”问题

我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？

设母鸡x只，公鸡y只，小鸡（100-x-y）只，
所以3x+5y+(100-x-y)/3=100
且x，y为整数，所以可以得出正确答案：
化简：8x+14y=200
有三种情况符合要求：
1.母鸡4只，公鸡12只，小鸡84只
2.母鸡11只，公鸡8只，小鸡81只
3.母鸡18只，公鸡4只，小鸡78只
"""

for num_cock in range(0, 20):
    for num_hen in range(0, 33):
        num_chicken = 100 - num_cock - num_hen
        if 14 * num_cock + 8 * num_hen - 200 == 0 and num_chicken > 0:
            print('公鸡：%d只，母鸡：%d只，小鸡：%d只' % (num_cock, num_hen, num_chicken))


"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...

斐波那契数列:1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
233，377，610，987，1597，2584，4181，6765，10946，17711，28657，46368........

这个数列从第3项开始，每一项都等于前两项之和。
"""

a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')


"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束
"""

money = 1000
while money > 0:
    print('你的总资产为：', money)
    needs_proceed = False
    while True:
        debt = int(input('请下注：'))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜')
        money -= debt
    else:
        needs_proceed = True

    while needs_proceed:
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
            needs_proceed = False
        elif current == first:
            print('玩家胜')
            money += debt
            needs_proceed = False

print('你破产了，游戏结束！')
