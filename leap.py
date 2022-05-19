#Python Program to Check Whether a Given Year is a Leap Year
def test():
year=input("Enter a year: ")
if ((year%400==0) or (year%100!=0) and (year%4==0)):
	print "This is leap year"
else:
	print "This is not a leap year"
test()
	