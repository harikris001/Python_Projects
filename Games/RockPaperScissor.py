from random import randint

entry = ["rock","paper","scissor"]
i = 0
j = 0


completed = False

while not completed:
	player = input("your play: ")
	cpu = entry[randint(0,2)]
	if player == cpu:
		print("Tie")
		print("Player :" + str(i) + " CPU :" + str(j))
	elif player in entry:
		if player == "rock":
			if cpu == "scissor":
				i+=1
				print("NICE PLAY \n Player :" + str(i) + " CPU :" + str(j))
			elif cpu == "paper":
				j+=1
				print("TRY AGAIN \n Player :" + str(i) + " CPU :" + str(j))
		elif player == "paper":
			if cpu == "rock":
				i+=1
				print("NICE PLAY \nPlayer :" + str(i) + " CPU :" + str(j))
			elif cpu == "scissor":
				j+=1
				print("TRY AGAIN \nPlayer :" + str(i) + " CPU :" + str(j) +" ")
		elif player == "scissor":
			if cpu == "paper":
				i+=1
				print("NICE PLAY \nPlayer :" + str(i) + " CPU :" + str(j))
			elif cpu == "rock":
				j+=1
				print("TRY AGAIN \nPlayer :" + str(i) + " CPU :" + str(j) +" ")
	else:
		print("Check the spelling")
	if j==3 or i==3:
		completed = True
if i==3:
	print("You win")
else :
	print("CPU win")
