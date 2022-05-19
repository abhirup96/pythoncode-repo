#Python Program to Find the Area of a Triangle Given All Three Sides
a=input("Enter the side1: ")
b=input("Enter the side2: ")
c=input("Enter the side3: ")
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print "The area of triangle is",area