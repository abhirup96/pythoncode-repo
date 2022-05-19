'''
Accept the electric units from user and calculate the bill according to the following rates.

First 100 Units     :  Free

Next 200 Units      :  Rs 2 per unit.

Above 300 Units    :  Rs 5 per unit.

if number of unit is 500 then total bill = 0 +400 + 1000 = 1400'''

unit=input("Enter the unit: ")
if(unit<=100):
	print"Free"
elif(unit>100 and unit<=200):
	bill=(unit-100)*2
	print"The total bill",bill
elif(unit>300):
	total=unit-300
	total2=total*5
	total3=400
	total4=total3+total2
	print"The total bill",total4