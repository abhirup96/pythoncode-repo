'''A company decided to give bonus to employee according to following criteria:

    Time period of Service                Bonus

    More than 10 years             10%

    >=6 and <=10                   8%

    Less than 6 years              5%

    Ask user for their salary and years of service and print the net bonus amount.'''

salary=input("Enter the salary: ")
year=input("Enter year of service: ")
if(year>10):
	n=10/100*salary
	print "The net bonus amount is",n
elif(year>=6 and year<=10):
	n=8/100*salary
	print "The net bonus amount is",n
elif(year<6):
	n=5/100*salary
	print "The net bonus amount is",n