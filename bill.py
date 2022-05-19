#Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
#             Unit                                                     Price
#First 100 units                                               no charge
#Next 100 units                                              Rs 5 per unit
#After 200 units                                             Rs 10 per unit
#(For example if input unit is 350 than total bill amount is Rs2000)
unit=input("Enter the unit: ")
if(unit<100):
	print "No charge"
elif(unit>100 and unit<=200):
	total=(unit-100)*5
	print "Total amount is:",total
elif(unit>200):
	total=unit-200
	total2=total*10
	total3=500
	total4=total2+total3
	print "Total amount is:",total4