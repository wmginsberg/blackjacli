import random


# Functions
def game_start():
	deck = make_deck()
	print 'Welcome to blackjack!   '
	name = raw_input('What is your name?   ')
	print 'Hi '+name+'! You are starting out with 100. The minimum bet is 10.'
	round_num = 1
	total_money = 100
	while (total_money >= 10):
		winnings,result,round_num = play_round(round_num,total_money,deck)
		if (result):
			total_money += winnings
			if (result == 1):
				continue
			elif (result == 2): 
				print 'Please place a bet greater than 10 and less than 100.'
				continue
			elif (result == 3):
				print 'Please bet only what you can afford.'
				continue
		else:
			total_money -= winnings


def play_round(round_num,total_money,deck):
	print ''
	print '--------- ROUND ' + str(round_num) + ' ---------'
	print 'Total: ' + str(total_money)
	bet = raw_input('Place bet (min: 10, max: 100)   ')
	winnings = 0
	result = 0
	# If there's a valid integer bet
	if (bet == 'quit'):
		print 'Goodbye!'
		exit()
	if (int(bet)):
		bet = int(bet)

		# If the bet is within the acceptable frame
		if (bet >= 10 and bet <= 100):

			if (bet >= total_money):
				result = 3

			# If the user wins: tell them, increase their score, increase the round 
			x = deal_cards(deck)
			if (x == 1):
				print 'You win!   +' + str(bet)
				winnings += bet
				result = 1
				round_num += 1
			elif (x == 2):
				print 'Push!   +0'
				result = 1
				round_num += 1

			# If the user loses: tell them, decrease their score, increase the round
			else:
				print 'You\'ve lost   -' + str(bet)
				winnings += bet
				result = 0
				round_num += 1
		
		elif (bet >= total_money):
			result = 3

		else:
			result = 2

	return winnings, result, round_num

def deal_cards(deck):
	random.shuffle(deck)
	dealer_down = deck[0]
	dealer_up = deck[1]
	player_one = deck[2]
	player_two = deck[3]
	dealer_ace = False
	player_ace = False
	print 'Dealer   :   [??????????????]' + '[' + dealer_up['title'] + ']'
	print 'Your hand:   [' + player_one['title'] + '][' + player_two['title'] + ']' 
	
	if (int(deck[0]['value']) == 11 or int(deck[1]['value']) == 11):
		dealer_ace = True
	if (int(deck[2]['value']) == 11 or int(deck[3]['value']) == 11):
		player_ace = True

	dealer_total = int(deck[0]['value']) + int(deck[1]['value'])
	if (dealer_total == 21):
		if (int(deck[0]['value']) == 11 and int(deck[1]['value']) == 10):
			print 'Dealer Blackjack!'
			return 0
		elif (int(deck[1]['value']) == 11 and int(deck[0]['value']) == 10):
			print 'Dealer Blackjack!'
			return 0

	player_total = int(deck[2]['value']) + int(deck[3]['value'])
	if (player_total == 21):
		if (int(deck[2]['value']) == 11 and int(deck[3]['value']) == 10):
			print 'You\'ve got Blackjack!'
			return 1
		elif (int(deck[3]['value']) == 11 and int(deck[2]['value']) == 10):
			print 'You\'ve got Blackjack!'
			return 1

	print 'Your total:   ' + str(player_total)
	i = 4
	while (True):
		move = raw_input('Hit or Stay? (h/s)   ')
		
		if (move == 's'):
			while (dealer_total < 17 or dealer_ace):
				dealer_total += int(deck[i]['value'])
				i += 1	
				if (dealer_ace):
					dealer_total -= 10
					dealer_ace = False
			if (dealer_total > 21):
				print 'Dealer bust!   ' + str(dealer_total)
				return 1
			if (dealer_total < 21 and dealer_total >= 17):
				print 'Dealer total:   ' + str(dealer_total)
				if (dealer_total < player_total):
					return 1
				elif (dealer_total > player_total):
					return 0
				else:
					return 2
		elif (move == 'h'):
			player_total += int(deck[i]['value'])
			i += 1		
			if (player_total > 21):
				if (player_ace):
					player_total -= 10
					player_ace = False
				else:
					print 'Player bust!   ' + str(player_total)
					return 0
			else:
				print 'Player total:   ' + str(player_total)


		else: 
			print 'Please type h or s, for Hit or Stay'

	return 1

def make_deck():
	values = ['11','2','3','4','5','6','7','8','9','10','10','10','10']
	cards = ['A ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10','J ','Q ','K ']
	suits = [' Spades','  Clubs',' Hearts','Diamonds']
	deck = []
	for c in range(12):
		for s in range(3):
			deck.append({ 'card' : cards[c], 
						  'suit' : suits[s], 
						  'value': values[c],
						  'title': cards[c] + ' of ' + suits[s]
						  })
	return deck



game_start()

