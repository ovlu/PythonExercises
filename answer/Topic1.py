```
1. 猜数字
经典的猜数字游戏，几乎所有人学编程时都会做。
功能描述： 随机选择一个三位以内的数字作为答案。用户输入一个数字，程序会提示大了或是小了，直到用户猜中。
```
import random
number = random.randint(1,100)
while True:
    col = int(input())
    if col == number:
        print("congratulations,number correct")
        break
    else:
        print("sorry,number error")