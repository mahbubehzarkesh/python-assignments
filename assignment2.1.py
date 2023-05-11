import math

while True :
    num1 = float(input("Enter a Number : "))
    op = input("Enter one of this Operators:   + , - , * , / ,  r for radical , sin , cos , tan , cot ,  f for factorial , exit) : ")
    if op=="r":
        result=math.sqrt(num1)
    if op=="sin":
        result=math.sin(math.radians(num1))
       
    if op=="cos":
        result=math.cos(math.radians(num1))
        
    if op=="tan":
        if math.radians(num1)==90 or math.radians(num1)==270:
            print("tan",num1,"is not defined")
        else : 
         result=math.tan(math.radians(num1))
        
    if op=="cot":
       if math.radians(num1)==0 or math.radians(num1)==180:
           print("cot",num1,"is not defined")
       else :
        result=math.tan(math.radians(num1))
       
    if op=="f" :
        num1=int(num1)
        result=math.factorial(num1)
    if op == "+":
        num2 = float(input("Enter the Second Number to add : "))
        result=num1+num2
    if op == "-":
        num2 = float(input("Enter the Second Number to subtract : "))
        result=num1-num2
    if op == "*":
        num2 = float(input("Enter the Second Number to multiply: "))
        result=num1*num2
    if op == "/":
        num2 = float(input("Enter your Second Number to divide : "))
        if num2==0:
            result = "error !!! you can not divide a number by zero"
        else :
            result=num1/num2
    if op == "exit":
        break
    print("the Result  is: ",result)