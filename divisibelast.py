#Write a program to check whether the last digit of a number( entered by user ) is 
divisible by 2 or not.
num=input("Enter the number: ")
num2=num%10
if(num2%2==0):
	print("The number is divisble by 2")
else:
	print("The number is not divisble by 2")