import random
while True:
    num = random.randint(1,6)
    print(num)
    if num== 6:
        print("you rock ... you can roll again")
        continue
    else:
        print("sorry ... you rolled number",num,"you can not continue")
        break

