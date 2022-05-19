#Accept 10 numbers from the user and display their average.

sum=0
for i in range (0,10):
	inp=input("Please enter 10 numbers: ")
	sum=sum+inp
print "The sum is",sum
avg=sum/10
print "The average is: ",avg
