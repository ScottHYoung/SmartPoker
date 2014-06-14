#---------------------------------------------------------------------------
#	card.py
#
#	Description:
#
#	Basic primitive for a playing card to be used as an object. Has a suit
#	(hearts, clubs, diamonds, spades) and a number (2-10,J,Q, K,A). Also includes
#   basic functions for comparing cards.
#
#---------------------------------------------------------------------------


#---------------------------------------------------------------------------
#	Card class
#	
#	Contains a suit, number and various comparison functions
#---------------------------------------------------------------------------
class Card:
	
	#---------------------------------------------------------------------------
	#	Constructor
	#
	#	Takes two strings, a suit and a number and creates the corresponding
	#	card. If either suit or number are ill-defined, the card will be undefined
	#---------------------------------------------------------------------------
	def __init__(self, newSuit, newNumber):	
		
		newNumber = newNumber.upper()
		
		if newNumber == "2":
			self.number = "2"
		elif newNumber == "3":
			self.number = "3"
		elif newNumber == "4":
			self.number = "4"
		elif newNumber == "5":
			self.number = "5"
		elif newNumber == "6":
			self.number = "6"
		elif newNumber == "7":
			self.number = "7"
		elif newNumber == "8":
			self.number = "8"
		elif newNumber == "9":
			self.number = "9"
		elif newNumber == "10":
			self.number = "10"
		elif newNumber == "J" or newNumber == "JACK":
			self.number = "J"
		elif newNumber == "Q" or newNumber == "QUEEN":
			self.number = "Q"
		elif newNumber == "K" or newNumber == "KING":
			self.number = "K"	
		elif newNumber == "A" or newNumber == "ACE" or newNumber == "1":
			self.number = "A"
		elif newNumber == "UNKNOWN" or newNumber == "?":
			self.number = "unknown"
		else:
			self.number = "undefined"
			
		newSuit = newSuit.lower()

		if newSuit == "hearts" or newSuit == "h":
			self.suit = "hearts"
		elif newSuit == "diamonds" or newSuit == "d":
			self.suit = "diamonds"
		elif newSuit == "clubs" or newSuit == "c":
			self.suit = "clubs"
		elif newSuit == "spades" or newSuit == "s":
			self.suit = "spades"
		elif newSuit == "unknown" or newSuit == "?":
			self.suit = "unknown"
		else:
			self.suit = "undefined"	
			
	
	#---------------------------------------------------------------------------
	#	isValid()
	#
	#	Returns true if the suit is not undefined. False if undefined.
	#---------------------------------------------------------------------------	
	def isValid(self):
		if self.suit != "undefined" and self.number != "undefined":

			#Assert that it is not some other string (should never happen)
			assert (self.suit == "hearts" or self.suit == "diamonds" or self.suit == "clubs" or self.suit == "spades" or self.suit == "unknown")
			assert (self.number == "2" or self.number == "3" or self.number == "4" or self.number == "5" or self.number == "6" or
					self.number == "7" or self.number == "8" or self.number == "9" or self.number == "10" or self.number == "unknown" or
					self.number == "J" or self.number == "Q" or self.number == "K" or self.number == "A")

			return True
		else:
			return False
			
	#---------------------------------------------------------------------------
	#	isMatch()
	#
	#	Returns true if the two cards have the same suit and number
	#---------------------------------------------------------------------------	
	def isMatch(self, card):
		
		if not (card.isValid() and self.isValid()):
			return False
		elif card.suit == self.suit and card.number == self.number:
			return True
		else:
			return False
			
				
	#---------------------------------------------------------------------------
	#	isColorMatch()
	#
	#	Returns true if the two cards are matching color
	#---------------------------------------------------------------------------	
	def isColorMatch(self, card):

		if self.suit == "hearts" or self.suit == "diamonds":
			color1 = "R"
		else:
			color1 = "B"
		
		if card.suit == "hearts" or card.suit == "diamonds":
			color2 = "R"
		else:
			color2 = "B"

		if not (card.isValid() and self.isValid()):
			return False
		elif color1 == color2:
			return True
		else:
			return False
			
	#---------------------------------------------------------------------------
	#	isPair()
	#
	#	Returns true if the cards are the same number
	#---------------------------------------------------------------------------	
	def isPair(self, card):
		
		return (card.isValid() and self.isValid()) and self.number == card.number	
		
	#---------------------------------------------------------------------------
	#	isSuited()
	#
	#	Returns true if the cards are the same number
	#---------------------------------------------------------------------------	
	def isSuited(self, card):

		return (card.isValid() and self.isValid()) and self.suit == card.suit
		
		
	#---------------------------------------------------------------------------
	#	isKnown()
	#
	#	Returns true if the card isn't unknown or undefined
	#---------------------------------------------------------------------------	
	def isKnown(self):

		return self.isValid() and self.suit != "unknown" and self.number != "unknown"		
		
#========================================
#	FUNCTIONS
#========================================					
			
				
#========================================
#	TESTS
#========================================	
	
if __name__ == '__main__':
	
	#UNIT TESTS
	print "Testing constructors"
	
	newCard = Card("hearts", "K")
	assert newCard.isValid()
	newCard = Card("diamonds", "king")
	assert newCard.isValid()
	newCard = Card("spades", "King")
	assert newCard.isValid()
	newCard = Card("clubs", "KING")
	assert newCard.isValid()
	
	newCard = Card("h", "Q")
	assert newCard.isValid()
	newCard = Card("d", "queen")
	assert newCard.isValid()
	newCard = Card("s", "Queen")
	assert newCard.isValid()
	newCard = Card("c", "QUEEN")
	assert newCard.isValid()
	
	newCard = Card("H", "ace")
	assert newCard.isValid()
	newCard = Card("D", "1")
	assert newCard.isValid()
	newCard = Card("S", "A")
	assert newCard.isValid()
	newCard = Card("C", "ACE")
	assert newCard.isValid()	
	
	newCard = Card("H", "2")
	assert newCard.isValid()
	newCard = Card("D", "3")
	assert newCard.isValid()
	newCard = Card("S", "4")
	assert newCard.isValid()
	newCard = Card("C", "5")
	assert newCard.isValid()
	newCard = Card("H", "6")
	assert newCard.isValid()
	newCard = Card("D", "7")
	assert newCard.isValid()
	newCard = Card("S", "8")
	assert newCard.isValid()
	newCard = Card("C", "9")
	assert newCard.isValid()
	newCard = Card("C", "10")
	assert newCard.isValid()
	
	newCard = Card("!", "!")
	assert not newCard.isValid()
	newCard = Card("h", "!")
	assert not newCard.isValid()
	newCard = Card("!", "2")
	assert not newCard.isValid()
	
	
	newCard = Card("C", "?")
	assert newCard.isValid()
	newCard = Card("unknown", "10")
	assert newCard.isValid()
	newCard = Card("?", "UNKNOWN")
	assert newCard.isValid()	
	newCard = Card("!", "UNKNOWN")
	assert not newCard.isValid()											
	
	print "Test successful."
	
	print "Testing isMatch()"
	
	card1 = Card("H", "A")
	card2 = Card("hearts", "1")
	assert card1.isMatch(card2)
	
	card1 = Card("!", "A")
	card2 = Card("!", "1")
	assert not card1.isMatch(card2)	
	
	card1 = Card("H", "A")
	card2 = Card("S", "1")
	assert not card1.isMatch(card2)	
	
	card1 = Card("spades", "J")
	card2 = Card("S", "1")
	assert not card1.isMatch(card2)	
	
	print "Test successful."
	
	print "Testing isColorMatch()"
	
	card1 = Card("H", "A")
	card2 = Card("D", "1")
	assert card1.isColorMatch(card2)
	
	card1 = Card("S", "A")
	card2 = Card("C", "1")
	assert card1.isColorMatch(card2)
	
	card1 = Card("S", "A")
	card2 = Card("S", "K")
	assert card1.isColorMatch(card2)
	
	card1 = Card("H", "A")
	card2 = Card("H", "K")
	assert card1.isColorMatch(card2)
	
	card1 = Card("!", "A")
	card2 = Card("H", "K")
	assert not card1.isColorMatch(card2)	
	
	card1 = Card("S", "A")
	card2 = Card("H", "K")
	assert not card1.isColorMatch(card2)
							
	print "Test successful."
	
	print "Testing isSuited()"
	
	card1 = Card("hearts", "A")
	card2 = Card("H", "K")
	assert card1.isSuited(card2)
	
	card1 = Card("diamonds", "A")
	card2 = Card("d", "K")
	assert card1.isSuited(card2)
	
	card1 = Card("hearts", "A")
	card2 = Card("D", "K")
	assert not card1.isSuited(card2)
	
	card1 = Card("!", "A")
	card2 = Card("H", "K")
	assert not card1.isSuited(card2)	
	
	print "Test successful."
	
	print "Testing isPair()"
	
	card1 = Card("D", "A")
	card2 = Card("H", "A")
	assert card1.isPair(card2)
	
	card1 = Card("S", "3")
	card2 = Card("d", "3")
	assert card1.isPair(card2)
	
	card1 = Card("D", "3")
	card2 = Card("D", "4")
	assert not card1.isPair(card2)
	
	card1 = Card("!", "A")
	card2 = Card("H", "A")
	assert not card1.isPair(card2)	
	
	print "Test successful."
	
	print "Testing isKnown()"
	
	card = Card("?", "?")
	assert not card.isKnown()	
	card = Card("h", "?")
	assert not card.isKnown()
	card = Card("?", "A")
	assert not card.isKnown()	
	card = Card("H", "10")
	assert card.isKnown()	
	card = Card("!", "!")
	assert not card.isKnown()
	
	print "Test successful."					