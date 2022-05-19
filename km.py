'''Accept the kilometers covered and calculate the bill according to the following criteria:

First 10 Km              Rs11/km

Next 90Km               Rs 10/km

After that               Rs9/km'''

km=input("Enter the km: ")
if(km<=10):
	total=km*11
	print "The bill is Rs", total
elif(km>10 and km<=100):
	total=km-10
	total2=10*11
	total3=total*10
	total4=total2+total3
	print "The bill is Rs", total4
elif(km>100):
	total=km-10
	total2=10*11
	total3=(total-100)*10
	total4=110*9
	total5=total4+total3
