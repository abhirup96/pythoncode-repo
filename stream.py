'''Accept the marks of English, Math and Science, Social Studies Subject and display the stream allotted according to following

All Subjects more than 80 marks —       Science Stream

English >80 and Math, Science above 50 –Commerce Stream

English > 80 and Social studies > 80    —   Humanities'''

e=input("Enter the marks in English: ")
m=input("Enter the marks in Math: ")
s=input("Enter the marks in Science: ")
ss=input("Enter the marks in Social Studies: ")
if(e>80 and m>80 and s>80 and ss>80):
	print"Science stream"
elif(e>80 and m>80 and ss>50 and s>=0):
	print"Commerce stream"
elif(e>80 and ss>80 and m>=0 and s>=0):
	print"Humanities"
