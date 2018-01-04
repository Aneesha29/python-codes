num=int(input("Enter a number between 1&100000: "))
if (num>=1)and(num<=100000):
	if (num%2==0):
		print ("Even")
elif (num%2!=0):
	print ("Odd")
else:
	print ("enter correct number")
