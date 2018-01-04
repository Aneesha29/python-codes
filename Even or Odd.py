#CHECK WEATHER EVEN OR ODD
num=int(input("Enter a number between 1&100000: "))
if num in range(1,100000):
	if (num%2==0):
		print ("Even")
	else:
		print ("Odd")
else:
	print ("Enter a correct number between 1&100000")
