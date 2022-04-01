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
