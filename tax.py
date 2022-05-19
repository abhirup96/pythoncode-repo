'''Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :

        Cost price (in Rs)                                       Tax
100000                                                            15 %
50000 and <= 100000                                10%
        <= 50000                                                      5%'''


price=input("Enter the cost price: ")
if(price==100000):
	print "Road tax is 15%"
elif(price==50000 or price<=100000):
	print "Road tax is 10%"
elif(price<=50000):
	print "Road tax is 5%"