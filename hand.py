#---------------------------------------------------------------------------
#	hand.py
#
#	Description:
#
#	Hand class takes a list of cards and an optional ID and evaluates it. 
#	Can be given any number of cards as a list to initialize, in order to
#	make valid poker hands of 5 cards
#---------------------------------------------------------------------------

import card

#---------------------------------------------------------------------------
#	Hand Class
#---------------------------------------------------------------------------
class Hand():
	
	#---------------------------------------------------------------------------
	#	Constructor
	#
	#	Given a list of cards and an optional id
	#---------------------------------------------------------------------------
	def __init__(self, cards, ID=-1):
		self.cards = cards
		self.id = ID	
		
	#---------------------------------------------------------------------------
	#	evaluate()
	#
	#	Takes the hand and evaluates it as a tuple of (rank, high1, high2, high3, high4, high5)
	#---------------------------------------------------------------------------
	def evaluate(self):
		
		#---------------------------------------------------------------------------
		#	Algorithm:
		#
		#	Straight-flush? (8, highest card, 0, 0, 0, 0)
		#	4-of-a-kind? (7, card in 4s, kicker, 0, 0, 0)
		#	Full house? (6, card in 3s, card in 2s, 0, 0, 0)
		#	Flush? (5, highest card, 2nd, 3rd, 4th, 5th)
		#	Straight? (4, highest card, 0, 0, 0, 0)
		#	3-of-a-kind? (3, card in 3s, kicker, 2nd, 0, 0)
		#	2 pairs? (2, high pair, low pair, kicker, 0, 0)
		#	Pair? (1, pair, kicker, 2nd, 3rd, 0)
		#	Nothing? (0, 1st, 2nd, 3rd, 4th, 5th)
		#
		#	All cards are stored by rank, which then uses tuple comparison to determine
		#	the greatest value
		#---------------------------------------------------------------------------
		
		cardsInStraightFlush = self.straightFlush()
		if cardsInStraightFlush != None:
			return (8, cardsInStraightFlush[0], 0, 0, 0, 0)
		
		cardsInFours = self.fourOfAKind()
		if cardsInFours != None:
			return (7, cardsInFours[0], cardsInFours[1], 0, 0, 0)
		
		cardsInFullHouse = self.fullHouse()
		if cardsInFullHouse != None:
			return (6, cardsInFullHouse[0], cardsInFullHouse[1], 0, 0, 0)
		
		cardsInFlush = self.flush()
		if cardsInFlush != None:
			return (5, cardsInFlush[0], cardsInFlush[1], cardsInFlush[2], cardsInFlush[3], cardsInFlush[4], cardsInFlush[5])
		
		cardsInStraight = self.straight()
		if cardsInStraight != None:
			return (4, cardsInStraight[0], 0, 0, 0, 0)
		
		cardsInThrees = self.threeOfAKind()
		if cardsInThrees != None:
			return (3, cardsInThrees[0], cardsInThrees[1], cardsInThrees[2], 0, 0)
			
		cardsInTwoPairs = self.twoPairs()
		if cardsInTwoPairs != None:
			return (2, cardsInTwoPairs[0], cardsInTwoPairs[1], cardsInTwoPairs[2], 0, 0)
			
		cardsInPair = self.pair()
		if cardsInPair != None:
			return (1, cardsInPair[0], cardsInPair[1], cardsInPair[2], cardsInPair[3], 0)
			
		cardsInHighCard = self.highCard()
		return (0, cardsInHighCard[0], cardsInHighCard[1], cardsInHighCard[2], cardsInHighCard[3], cardsInHighCard[4], cardsInHighCard[5])
		
	#--------------------------------------------------------------------------
	#	straightFlush()
	#--------------------------------------------------------------------------	
	def straightFlush(self):
		return []
		
	#--------------------------------------------------------------------------
	#	fourOfAKind()
	#--------------------------------------------------------------------------	
	def fourOfAKind(self):
		return []
				
	#--------------------------------------------------------------------------
	#	fullHouse()
	#--------------------------------------------------------------------------	
	def fullHouse(self):
		return []
		
	#--------------------------------------------------------------------------
	#	flush()
	#--------------------------------------------------------------------------	
	def flush(self):
		return []

	#--------------------------------------------------------------------------
	#	straight()
	#--------------------------------------------------------------------------	
	def straight(self):
		return []	
		
	#--------------------------------------------------------------------------
	#	threeOfAKind()
	#--------------------------------------------------------------------------	
	def threeOfAKind(self):
		return []
	
	#--------------------------------------------------------------------------
	#	twoPairs()
	#--------------------------------------------------------------------------	
	def twoPairs(self):
		return []	
		
	#--------------------------------------------------------------------------
	#	pair()
	#--------------------------------------------------------------------------	
	def pair(self):
		return []	
		
	#--------------------------------------------------------------------------
	#	highCard()
	#--------------------------------------------------------------------------	
	def straightFlush(self):
		return []							
#--------------------------------------------------------------------------
#	Class Functions 
#--------------------------------------------------------------------------	


#--------------------------------------------------------------------------
#	Winner()
#
#	Evaluates a list of hand objects and returns the id of the winning hand
#--------------------------------------------------------------------------
def winner(hands):
	
	winningID = hands[0].id#-1
	
	return winningID
		