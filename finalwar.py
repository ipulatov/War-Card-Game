import random
Heart_cards = ["1 of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts"]
Club_cards = ["1 of Clubs", "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs", "7 of Clubs", "8 of Clubs", "9 of Clubs", "10 of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs"]
Spade_cards = ["1 of Spades", "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades", "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades", "Jack of Spades", "Queen of Spades", "King of Spades"]
Diamond_cards = ["1 of Diamonds", "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds"]


names = Heart_cards + Club_cards + Spade_cards + Diamond_cards
values = [14,2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,]

working_names = names.copy()
shuffled_working_names = random.sample(working_names, len(working_names))

player1_deck = shuffled_working_names[0:26]
computer_deck = shuffled_working_names[26:]
war_deck=[]

player1_count = 0
computer_count = 0
count_in_a_tie = 0  
second_to_last_tie = 0
move_number = 1
def function(card1, card2):
	global move_number
	print("\nMove number:")
	input(move_number)
	move_number+=1
	place_of_i_for_card_1 = names.index(card1)
	value_we_want_for_card1 = values[place_of_i_for_card_1]
	place_of_i_for_card_2 = names.index(card2)
	value_we_want_for_card2 = values[place_of_i_for_card_2]
	global war_deck
	global count_in_a_tie
	global player1_count
	global computer_count
	global second_to_last_tie
	if value_we_want_for_card1 > value_we_want_for_card2:
		print("\nYour card:", card1, "\nComp's card:", card2, "\nYou win")
		#global player1_count
		if len(war_deck) == 0:
			player1_count=player1_count+ 2 + second_to_last_tie
			second_to_last_tie = 0 
		
		if len(war_deck) != 0:
			player1_count= player1_count + len(war_deck) + count_in_a_tie + second_to_last_tie + 2
			war_deck = []
			count_in_a_tie = 0
			second_to_last_tie= 0
		#print("Your count is now", player1_count, ", and the computer's count is", computer_count, ".")
	elif value_we_want_for_card1 < value_we_want_for_card2:
		print("\nYour card:", card1, "\nComp's card:", card2, "\nComputer wins")

		if len(war_deck) == 0:
			computer_count=computer_count+ 2 + second_to_last_tie
			second_to_last_tie= 0
		if len(war_deck) != 0:
			computer_count=computer_count+len(war_deck)+count_in_a_tie + second_to_last_tie + 2
			war_deck = []
			count_in_a_tie = 0
			second_to_last_tie= 0
		#print("Your count is now", player1_count, ", and the computer's count is", computer_count, ".")
		
	elif value_we_want_for_card1 == value_we_want_for_card2:

		x = len(player1_deck)
		y = len(computer_deck)
		if x==0 and y==0:
			print("Well, this is epic. You drew", card1, ", and the computer drew", card2, ". You both get to keep the cards you just drew, plus everything else.")
			computer_count = computer_count + 1 + count_in_a_tie/2 + len(war_deck)/2
			player1_count = player1_count + 1 + count_in_a_tie/2 + len(war_deck)/2
						
		if x > 1 and y > 1:
		
			card3 = player1_deck[0]
			player1_deck.remove(card3)
			war_deck.append(card3)
				
			card6 = computer_deck[0]
			computer_deck.remove(card6)
			war_deck.append(card6)
							
			if x > 2 and y > 2: 
			
				card4 = player1_deck[0]
				player1_deck.remove(card4)
				war_deck.append(card4)
				
				card7 = computer_deck[0]
				computer_deck.remove(card7)
				war_deck.append(card7)
								
				if x > 3 and y > 3: 
				
					card5 = player1_deck[0]
					player1_deck.remove(card5)
					war_deck.append(card5)
		
					card8 = computer_deck[0]
					computer_deck.remove(card8)
					war_deck.append(card8)
					
		count_in_a_tie += 2
		
		if x==1 and y==1:
			second_to_last_tie+=2
			count_in_a_tie -= 2	
		if len(war_deck) == 0 and len(player1_deck) == 0 and len(computer_deck) == 0:

			player1_count+=1
			computer_count+=1
			print("You seem to have tied on the last move. Your card was", card1, "and the computer's card was", card2, ".You both get to keep your cards.")
		
		if len(war_deck)/2 != 0:
			if len(player1_deck)!=0 and len(computer_deck)!=0:
				print("\nIt's a tie , between", card1, "and", card2,  ".\n\nWe've taken", len(war_deck)/2, "total face-down cards from each of you, and now we have to do a war.")
	print("\nYour count:", player1_count)
	print("Computer's count:", computer_count)
	
while player1_count + computer_count != 52:	
	if len(war_deck) ==0:
		if player1_count == 0 and computer_count==0:
			input("Hi, you are playing war against a computer. We've shuffled both your decks already. Hit 'Enter' to start.")
	card1 = player1_deck[0]
	player1_deck.remove(card1)
	card2 = computer_deck[0]
	computer_deck.remove(card2)
	function(card1, card2)
	
if player1_count + computer_count == 52:
	input()
	print("Game over.\nYou have a count of", player1_count, "and the computer has a count of", computer_count, ".")
	if player1_count>computer_count:
		print("So you won, congrats :) \n")
	elif computer_count>player1_count:
		print("So the computer won, :( \n ")
	elif computer_count==player1_count:
		print("You both tied, so... idk try again.\n")
