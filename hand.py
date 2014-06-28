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

#--------------------------------------------------------------------------
#	Class Functions 
#--------------------------------------------------------------------------	


#--------------------------------------------------------------------------
#	Winner()
#
#	Evaluates a list of hand objects and returns the id of the winning hand
#--------------------------------------------------------------------------
def winner(hands):
	
	#Currently just returns the first hand in the bunch
	return hands[0].id
		