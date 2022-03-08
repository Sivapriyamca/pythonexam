from math import pi
n=int(input("**********  ENTER 1 FOR FINDING TRIANGLE AREA ___,  "
            "***********  ENTER 2 FOR FINDING RECTANGLE AREA ___,  "
            "************  ENTER 3 FOR FINDING CIRCLE AREA ___:"))
if n==1:
    b = float(input("enter the base length of triangle:"))
    h = float(input("enter height of the triangle:"))
    area = 1 / 2 * b * h
    print("area of given triangle is:", area)
elif n==2:
    l = float(input("enter the length of rectangle:"))
    b1 = float(input("enter the breadth of rectangle:"))
    area1 = l * b1
    print("area of rectangle is:", area1)
elif n==3:
     r = float(input("enter the radius of circle:"))
     area2 = pi * r * r
     print("area of circle is :", area2)
else:
    print("***your choice is wrong***")
