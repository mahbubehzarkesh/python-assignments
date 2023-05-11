import random

i = 0
arr = []
array_length = int(input("enter the length of the list :"))
n=int(input("enter the greater number  that you want to have  in your list: "))
while True:
    if i != array_length:
        number = random.randint(1,n)
        if i== 0:
            arr.append(number)
            i += 1
        else: 
          for i in range(len(arr)):
                if number != arr[i]:
                    if i == len(arr) - 1:
                        arr.append(number)
                        i += 1
                    else:
                        continue
                else:
                    continue
    else:
        break
    
print(arr)