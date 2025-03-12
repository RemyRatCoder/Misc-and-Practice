import time
from random import randrange
playagain = 'yes'

while playagain.lower() == 'yes':
	turn = 1
	winlose = "none"
	diffchoice = input("Choose difficulty (easy, medium, hard): ")
	easydiff = {'guesses': 3, 'range': 11}
	meddiff = {'guesses': 6, 'range': 51}
	harddiff = {'guesses': 9, 'range': 101}

	if diffchoice.lower() == "easy":
		difficulty = easydiff
	elif diffchoice.lower() == "medium":
		difficulty = meddiff
	elif diffchoice.lower() == "hard":
		difficulty = harddiff

	answer = (randrange(1,difficulty['range'] - 1))

	time.sleep(1)

	print("Let's play a game!")
	time.sleep(1)
	print("I'm thinking of a number...")
	time.sleep(1)
	print("It's between 1 and " + str(difficulty['range'] - 1) + ".")
	time.sleep(1)
	print("You have " + str(difficulty['guesses']) + " guesses.")
	time.sleep(1)
	guess = input("What's your first guess? ")
	turn += 1

	while winlose not in ('win','lose'):
		if int(guess) < answer and answer > 0:
			print("NOPE! Too low.")
			if turn > difficulty['guesses']:
				winlose = "lose"
				break
			time.sleep(1)
			guess = input("What's your next guess? ")
			turn += 1
		elif int(guess) > answer and answer < difficulty['range'] - 1:
			print("NO WAY! Too high!")
			if turn > difficulty['guesses']:
				winlose = "lose"
				break
			time.sleep(1)
			guess = input("What's your next guess? ")
			turn += 1
		elif str(guess) == str(answer):
			print("Oh my gosh! You guessed it!!")
			time.sleep(1)
			winlose = "win"
			
	
	
	if winlose == "win":
		playagain = input("You beat me! Want to play again? ")
	elif winlose == "lose":
		print("Wrong! The number was " + str(answer) + ".")
		playagain = input("I win, you lose! Want to play again? ")

