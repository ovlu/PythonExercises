// 最冗余的代码猜测数字
//后续查看其他方法，补全逻辑
a = int(input())
number = 0
num = 0
while True:
    
    if number == a:
        print("you input sumber is",number,",共猜测了",num,"次")
        break
    else:
        number=number+1
        num = num+1
//代码更新，更换方式
//使用随机random赋予随机数猜测
from random import randint
while True:
    try:
        num = int(input())
        if 1 <= num <= 100:
            if isinstance(num,int):
                break
            else:
                print('你输入的不是范围内的正整数')
                continue
        else:
            print('你输入的不是范围内的正整数')
            continue
    except ValueError:
        print('你输入的不是范围内的正整数')
        continue
guess=randint(1,100)
rom = 0
step = 0
while guess != num:
    if guess < num:
        step+=1
        print('我猜你输入的是:{}，偏小。'.format(guess))
        guess = randint(guess+1,100)
    if guess > num:
        step+=1
        print('我猜你输入的是:{}，偏大。'.format(guess))
        guess = randint(1,guess-1)
print('我猜到了，你一定输入的是{},我一共猜了{}次。'.format(guess, step))
