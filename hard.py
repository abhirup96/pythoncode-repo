'''user=input("Enter the unit: ")
if(user<=200):
	print "No charge"
elif(user>200 and user<=400):
	total=(user-200)*10
	print "The total is:",total
elif(user>400 and user<=600):
	total=2000+(user-400)*5
	print "The total is:",total'''

'''user=input("Enter the unit: ")
if(user<=30):
	print "No charge"
elif(user>30 and user<=37):
	total=user*2.5
	print "The total is",total
elif(user>37 and user<=42):
	total=12.5+(user-37)*3.5
	print "The total is",total
elif(user>42 and user<=50):
	total=12.5+17.5+(user-42)
	print "The total is", total'''


cost=input("Enter the cost: ")
if(cost<1000):
	print "No discount"
elif(cost>1000 and cost<=2000):
	total=(10/100)*cost
	print "The total is",total
elif(cost>2000 and cost<=3000):
	total=(20/100)*cost
	print "The total is",total
elif(cost>3000):
	total=(30/100)*cost
	print "The total is",total
