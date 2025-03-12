import time
from random import randrange
rollagain = 'yes'

while rollagain.lower() == 'yes':
	num = 0
	sides = input("Enter the number of sides the dice has: ")
	rolls = input("Enter the number of dice rolls to perform: ")

	if int(rolls) < 2:
		print(randrange(1,(int(sides) + 1)))
	elif int(rolls) > 1:
		while num < int(rolls):
			print(randrange(1,(int(sides) + 1)))

			num += 1
			time.sleep(0.5)
			
	rollagain = input("Roll another dice? ")
