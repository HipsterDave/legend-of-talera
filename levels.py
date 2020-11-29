import functions
import text
import sys
import time
import random
import os

trophies = []

def waiting_room():
	typing("Ah, welcome back! You either lost or won.\n")
	guides = ["Alice", "Jerry", "Brian", "Rachel"]
	randomguide = random.choice(guides)
	typing("Welcome to Talera waiting room! Today, " + randomguide + " will be your guide.\n")
	typing(randomguide + " - Let's see what trophies you currently have.\n")
	typing("Your trophies are:\n")
	for t in trophies:
		typing(t + "\n")
	text.levels()
	levelpick = ""
	while levelpick not in ["1"]:
		levelpick = input("> ")
	if levelpick == "1":
		mines()

typingspeed = 100

def clear():
	os.system("cls")

def typing(text):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10/typingspeed)

def settype(text, typing_speed):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10/typing_speed)

def mines():
	clear()
	typing("Before we travel to THE MINES, we need to set your levels.\n")
	time.sleep(1)
	clear()
	global speed
	global charisma
	global strength
	global knowledge
	functions.textloding(3, "Rolling Dice")
	levelnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	knowledge = random.choice(levelnumbers)
	strength = random.choice(levelnumbers)
	charisma = random.choice(levelnumbers)
	speed = random.choice(levelnumbers)
	typing("Your knowledge level is " + str(knowledge) + ".\n")
	typing("Your strength level is " + str(strength) + ".\n")
	typing("Your charisma level is " + str(charisma) + ".\n")
	typing("Your speed level is " + str(speed) + ".\n")
	averageleveladd = knowledge + strength + charisma + speed
	averageleveldivide = averageleveladd/4
	typing("Your average level is " + str(averageleveldivide) + ".\n")
	typing("Please press enter to continue.\n")
	input("> ")
	clear()
	functions.textloding(3, "Traveling to THE MINES")
	typing("Welcome to THE MINES! Today, your goal is the get the famous TALREA RUBY.\n")
	typing("You will need to get past rock monsters and big avalanches.\n")
	typing("Let's begin!\n")
	typing("As you walk to the entrance of the mine, you realize that your mine pass has expired. You are not allowed to go in the mines without one.\n")
	typing("You do have the chance to convince the worker to let you in. You need a charisma level above 3 to do that.\n")
	typing("You can also try to sneak in. If it goes wrong, you will spend the rest of your life in prison.\n")
	text.mine_entrance()
	entrance = ""
	while entrance not in ("1", "2"):
		entrance = input("> ")
	if entrance == "1":
		clear()
		if charisma >= 4:
			typing("You sucessfully convinced the worker to let you in.\n")
			mines_again()
		else:
			typing("You were unable to convince the worker to let you in. You walk away in defeat.\n")
			text.youlost()
			functions.waitingroom_teleport()
	elif entrance == "2":
		clear()
		typing("You attempt to sneak in.\n")
		typing("Right as you sneak in to the mine, a police officer sees you.\n")
		typing("Quick! We need to do something!\n")
		text.policeoptions()
		police_options = ""
		while police_options not in ["1", "2", "3", "4"]:
			police_options = input("> ")
		if police_options == "1":
			clear()
			typing("You attempt to run away.\n")
			if speed >= 5:
				typing("Since you have a speed level of over 4, you are pretty fast. The policeman is no match for you.\n")
				mines_again()
			else:
				typing("You have a speed level under 4. You are so slow! The policeman catches you, and you get put in jail forever.\n")
				text.youlost()
				functions.waitingroom_teleport()
		if police_options == "2":
			clear()
			typing("You attempt to negotiate.\n")
			typing("You REALLY think you are going to get away with this? I THINK NOT!\n")
			text.youlost()
			functions.waitingroom_teleport()
		if police_options == "3":
			clear()
			typing("You attempt to hide.\n")
			if knowledge >= 4:
				typing("Since you have a knowledge level of over 3, you at least know a good place to hide.\n")
				mines_again()
			else:
				typing("You have a knowledge level under 3.\n")
				typing("You are pretty dumb, because you for some reason you hid behind the police officer.\n")
				text.youlost()
				functions.waitingroom_teleport()
		if police_options == "4":
			clear()
			typing("You attempt to fight.\n")
			if strength >= 5:
				typing("Since you have a strength level over 4, you are pretty strong. That police man was no match for you.\n")
				mines_again()
			else:
				typing("Why do you even try? You arms are like floppy noodles!\n")
				text.youlost()
				functions.waitingroom_teleport()

def mines_again():
	typing("As you walk through the mine, you see green gems, yellow gems, blue gems, but no TALERA RUBY.\n")
	typing("Then, you see a giant glimmering ruby sitting in a glass cage.\n")
	text.rubysteal()
	glass = ""
	while glass not in ["1", "2", "3"]:
		glass = input("> ")
	if glass == "1":
		clear()
		typing("You attempt to break the glass with a stone.\n")
		typing("BEEP BEEP BEEP! An alarm sounds and a rock monster comes out of the cave.\n")
		text.rockmonster()
		rockmonster = ""
		while rockmonster not in ["1", "2"]:
			rockmonster = input("> ")
		if rockmonster == "1":
			clear()
			typing("You attempt to fight the rock monster.\n")
			if strength >= 7:
				typing("WOW! You have a strength level of over 6! You successfully defeated the rock monster!\n")
				typing("You obtain the TALERA RUBY!\n")
				typing("As you run for the exit of the mine, an AVALANCHE starts!\n")
				text.avalanche()
				avalanche = ""
				while avalanche not in ["1", "2", "3"]:
					avalanche = input("> ")
				if avalanche == "1":
					clear()
					typing("You attempt to run.\n")
					if speed == 10:
						typing("WHAT??? You have a speed level of 10! You successfully made it out of the cave.\n")
						if "Talera Ruby" not in trophies:
							trophies.append("Talera Ruby")
							typing("You obtained the TALERA RUBY!\n")
							text.youwon()
							typing("You may have won, but you can also get the shattered ruby pieces.\n")
							functions.waitingroom_teleport()
						else:
							typing("Seems like you already have the TALERA RUBY inside your trophy room...\n")
							text.youwon()
							functions.waitingroom_teleport()
					else:
						typing("The avalanche was too fast...\n")
						text.youlost()
						functions.waitingroom_teleport()
				elif avalanche == "2":
					clear()
					typing("You attempt to find a safe place to hide.\n")
					typing("You find a big rock to hide under.\n")
					typing("The avalanche ends.\n")
					if "Talera Ruby" not in trophies:
						trophies.append("Talera Ruby")
						typing("You obtained the TALERA RUBY!\n")
						text.youwon()
						typing("You may have won, but you can also get the shattered ruby pieces.\n")
						functions.waitingroom_teleport()
					else:
						typing("Seems like you already have the TALERA RUBY inside your trophy room...\n")
						functions.waitingroom_teleport()
				elif avalanche == "3":
					clear()
					typing("You attempt to shield yourself with the ruby.\n")
					typing("As the rocks fall on the ruby, it shatters to pieces.\n")
					typing("Still, you have made it out of the mines.\n")
					if "Shattered Ruby Pieces" not in trophies:
						trophies.append("Shattered Ruby Pieces")
						typing("You obtained the SHATTERED RUBY PIECES!\n")
						text.youwon()
						typing("You may have won, but you can still get the full ruby.\n")
						functions.waitingroom_teleport()
					else:
						typing("Seems like you already have the SHATTERED RUBY PIECES inside your trophy room...\n")
		elif rockmonster == "2":
			clear()
			typing("You ran away from the monster, but you forgot one key item...\n")
			typing("THE RUBY.\n")
			text.youlost()
			functions.waitingroom_teleport()
	elif glass == "2":
		clear()
		typing("You attempt to slowly lift up the glass.\n")
		typing("You obtain the TALERA RUBY!\n")
		typing("As you run for the exit of the mine, an AVALANCHE starts!\n")
		text.avalanche()
		avalanche = ""
		while avalanche not in ["1", "2", "3"]:
			avalanche = input("> ")
		if avalanche == "1":
			clear()
			typing("You attempt to run.\n")
			if speed == 10:
				typing("WHAT??? You have a speed level of 10! You successfully made it out of the cave.\n")
				if "Talera Ruby" not in trophies:
					trophies.append("Talera Ruby")
					typing("You obtained the TALERA RUBY!\n")
					text.youwon()
					typing("You may have won, but you can also get the shattered ruby pieces.\n")
					functions.waitingroom_teleport()
				else:
					typing("Seems like you already have the TALERA RUBY inside your trophy room...\n")
					text.youwon()
					functions.waitingroom_teleport()
			else:
				typing("The avalanche was too fast...\n")
				text.youlost()
				functions.waitingroom_teleport()
		elif avalanche == "2":
			clear()
			typing("You attempt to find a safe place to hide.\n")
			typing("You find a big rock to hide under.\n")
			typing("The avalanche ends.\n")
			if "Talera Ruby" not in trophies:
				trophies.append("Talera Ruby")
				typing("You obtained the TALERA RUBY!\n")
				text.youwon()
				typing("You may have won, but you can also get the shattered ruby pieces.\n")
				functions.waitingroom_teleport()
			else:
				typing("Seems like you already have the TALERA RUBY inside your trophy room...\n")
				functions.waitingroom_teleport()
		elif avalanche == "3":
			clear()
			typing("You attempt to shield yourself with the ruby.\n")
			typing("As the rocks fall on the ruby, it shatters to pieces.\n")
			typing("Still, you have made it out of the mines.\n")
			if "Shattered Ruby Pieces" not in trophies:
				trophies.append("Shattered Ruby Pieces")
				typing("You obtained the SHATTERED RUBY PIECES!\n")
				text.youwon()
				typing("You may have won, but you can still get the full ruby.\n")
				functions.waitingroom_teleport()
			else:
				typing("Seems like you already have the SHATTERED RUBY PIECES inside your trophy room...\n")
	elif glass == "3":
		clear()
		typing("You admire the ruby.\n")
		time.sleep(1)
		functions.textloding(3, "Admiring the TALERA RUBY")
		typing("How is this going to help?\n")
		text.youlost()
		functions.waitingroom_teleport()

def forest():
	clear()
	typing("Before we travel to THE FOREST, we need to set your levels.\n")
	time.sleep(1)
	clear()
	functions.textloding(3, "Rolling Dice")
	levelnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	knowledge = random.choice(levelnumbers)
	strength = random.choice(levelnumbers)
	charisma = random.choice(levelnumbers)
	speed = random.choice(levelnumbers)
	typing("Your knowledge level is " + str(knowledge) + ".\n")
	typing("Your strength level is " + str(strength) + ".\n")
	typing("Your charisma level is " + str(charisma) + ".\n")
	typing("Your speed level is " + str(speed) + ".\n")
	averageleveladd = knowledge + strength + charisma + speed
	averageleveldivide = averageleveladd/4
	typing("Your average level is " + str(averageleveldivide) + ".\n")
	typing("Please press enter to continue.\n")
	input("> ")
	clear()
	functions.textloding(3, "Traveling to THE FOREST")
	typing("Welcome to THE FOREST! Today, your goal is to get the ELVERN FLUTE.\n")
	typing("Let's begin!\n")
	typing("For this adventure, you need to choose a weapon. This will affect the game later on.\n")
	text.weapon_forest()
	weapon = ""
	while weapon not in ["1", "2", "3"]:
		weapon = input("> ")
	if weapon == "1":
		clear()
		typing("You have chosen the sword. Good choice!\n")
	elif weapon == "2":
		clear()
		typing("Nice! You chose the bow!\n")
	elif weapon == "3":
		clear()
		typing("The mace is a good choice!\n")
	typing("As you walk through the forest trail, you see many trees and flowers.\n")
	typing("Then, you see a sign. Would you like to read it? (y/n)\n")
	sign = ""
	while sign not in ["y", "n"]:
		sign = input("> ")
	if sign == "y":
		clear()
		typing("You read the sign. It reads:\n\n")
	elif sign == "n":
		clear()
		typing("You do not read the sign. It might have important information that will affect you later on.\n")
	typing("You continue on the road.\n")