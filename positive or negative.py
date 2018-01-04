#CHECKE WHEATHER NUMBER IS POSITIVE OR NEGATIVE
num=int(input("Enter a number between 1&10000: "))
if (num>=1)and(num<=100000):
	print ("Positive")
elif (num<0):
	print ("Negative")
else:
	print ("0")
