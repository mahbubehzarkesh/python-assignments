side1=int(input("please enter a number for side1 of triangle:"))
side2=int(input("please enter a number for side2 of triangle:"))
side3=int(input("please enter a number for side3 of triangle:"))
if (side1<side2+side3 ) and (side2<side1+side3) and (side3<side1+side2):
    print("you can draw a triangle with these sides")
else:
    print("you can not draw a triangle with these sides")
