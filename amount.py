'''Accept the marked price from the user and  calculate the Net amount as(Marked Price –    Discount) to pay according to following criteria:

Marked Price    Discount
>10000    20%
>7000 and <=10000    15%
<=7000    10
price=input("Enter the marked price: ")
if(price>10000):
	amount=price-20/100
	print "The net amount is :",amount
elif(price>7000 and price<=10000):
	amount=price-15/100
	print "The net amount is :",amount
elif(price<=7000):
	amount=price-10/100
	print "The net amount is :",amount

