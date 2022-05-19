'''
Write a program to accept percentage from the user and display the grade according to the following criteria:

         Marks                                    Grade
90                                                   A
80 and <= 90                               B
       >= 60 and <= 80                      C
      below 60                                      D'''
p=input("Enter the percentage: ")
if(p==90):
	print "Your Grade is A"
elif(p>80 and p<=90):
	print "Your Grade is B"
elif(p>=60 and p<=80):
	print "Your Grade is C"
elif(p<60):
	print "Your Grade is D"