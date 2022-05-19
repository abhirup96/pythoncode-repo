# Write a program to check voter eligibility
name=raw_input("Enter your name: ")
age=input("Enter your age: ")

if(age<18):
	print "Hi ",name, "You are not eligible to vote"
elif(age>=18):
	print "Hi ",name
	print "You are eligible to vote"
