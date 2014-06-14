#---------------------------------------------------------------------------
#	state.py
#
#	Description:
#
#	Current game state available to a player. 
#
#	- List of playerInfo for all players:
#		- ID
#		- Name
#		- Pocket cards (unknown if not revealed yet)
#		- Bank (how much the person has in chips (doesn't include money in pot))
#		- Amount in pot (how much the person has put into the pot)
#		- Turn order (BB, SB, Dealer, etc.) (-1 meaning bankrupted)
#		- Active turn (if not active turn, only viable player decision is "Wait")
#	- Community cards
#	- Miscellaneous information
#	
#
#---------------------------------------------------------------------------

from player import PlayerInfo
import card

#---------------------------------------------------------------------------
#	State class
#---------------------------------------------------------------------------
class State():
	
	#---------------------------------------------------------------------------
	#	Constructor
	#
	#	Takes a list of playerInfo, a list of community cards and a list of strings
	#	for miscellaneous information which can be resized as needed
	#---------------------------------------------------------------------------
	def __init__(self, playersInfo, communityCards, miscInfo = []):
		
		self.playersInfo = playersInfo
		self.communityCards = communityCards
		self.miscInfo = miscInfo
		
	#---------------------------------------------------------------------------
	#	isValid
	#
	#	Runs through the game state to ensure that the state upholds the rules
	#	of Texas Hold'em. 
	#---------------------------------------------------------------------------
	def isValid(self):
		
		# Confirm all players have valid information
		if len(self.playersInfo) > 2:
			activePlayers = 0
			ids = []
			turnOrders = []
			for playerInfo in self.playersInfo:
				
				if playerInfo.activeTurn:
					activePlayers += 1
				
				if not playerInfo.id in ids:
					ids.append(playerInfo.id)
				
				if not playerInfo.isValid():
					return False
					
				if playerInfo.turnOrder >= 0:
					turnOrders.append(playerInfo.turnOrder)
					
			#Someone must be the active player!		
			if activePlayers != 1:
				return False
				
			#All ids must be unique	
			if not len(ids) == len(self.playersInfo):
				return False
				
			#Turn orders must be exactly 0, 1, 2, ...
			i = 0
			turnOrders.sort()
			for turn in turnOrders:
				if i != turn:
					return False
				i += 1
						
					
		else:
			return False
		
		# Confirm community cards are valid
		if len(self.communityCards) <= 5:
			if len(self.communityCards) > 0:
				
				for card in self.communityCards:
					if not card.isValid() or not card.isKnown():
						return False
						
		else:
			return False
			
		#Passed all checks, is a valid game state	
		return True
						



#========================================
#	TESTS
#========================================
if __name__ == '__main__':

	#UNIT TESTS
	print "Testing constructors."
	
	player1 = PlayerInfo(0, "John", 0, 100, 10, [card.Card("H", "3"), card.Card("S", "2")], False)			
	player2 = PlayerInfo(1, "Susy", 1, 100, 5, [card.Card("?", "?"), card.Card("?", "?")], False)
	player3 = PlayerInfo(2, "Hamm", 2, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], False)
	player4 = PlayerInfo(3, "Gunn", 3, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], True)
	
	infos = [player1, player2, player3, player4]
	
	state = State(infos, [])	
	
	assert state.isValid()
	
	#Here the turn orders aren't well formed
	player1 = PlayerInfo(0, "John", 0, 100, 10, [card.Card("H", "3"), card.Card("S", "2")], False)			
	player2 = PlayerInfo(1, "Susy", 1, 100, 5, [card.Card("?", "?"), card.Card("?", "?")], False)
	player3 = PlayerInfo(2, "Hamm", 1, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], False)
	player4 = PlayerInfo(3, "Gunn", 3, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], True)
	
	infos = [player1, player2, player3, player4]
	
	state = State(infos, [])	
	
	assert not state.isValid()
	
	#Here the ids aren't unique
	player1 = PlayerInfo(0, "John", 0, 100, 10, [card.Card("H", "3"), card.Card("S", "2")], False)			
	player2 = PlayerInfo(0, "Susy", 1, 100, 5, [card.Card("?", "?"), card.Card("?", "?")], False)
	player3 = PlayerInfo(2, "Hamm", 2, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], False)
	player4 = PlayerInfo(3, "Gunn", 3, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], True)
	
	infos = [player1, player2, player3, player4]
	
	state = State(infos, [])	
	
	assert not state.isValid()	
	
	#Here there is no active player
	player1 = PlayerInfo(0, "John", 0, 100, 10, [card.Card("H", "3"), card.Card("S", "2")], False)			
	player2 = PlayerInfo(1, "Susy", 1, 100, 5, [card.Card("?", "?"), card.Card("?", "?")], False)
	player3 = PlayerInfo(2, "Hamm", 2, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], False)
	player4 = PlayerInfo(3, "Gunn", 3, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], False)
	
	infos = [player1, player2, player3, player4]
	
	state = State(infos, [])	
	
	assert not state.isValid()	
	
	#Here there are too many community cards
	player1 = PlayerInfo(0, "John", 0, 100, 10, [card.Card("H", "3"), card.Card("S", "2")], False)			
	player2 = PlayerInfo(1, "Susy", 1, 100, 5, [card.Card("?", "?"), card.Card("?", "?")], False)
	player3 = PlayerInfo(2, "Hamm", 2, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], False)
	player4 = PlayerInfo(3, "Gunn", 3, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], True)
	
	infos = [player1, player2, player3, player4]
	
	cards = [card.Card("H", "A"),card.Card("S", "A"),card.Card("H", "2"),card.Card("H", "3"),card.Card("H", "4"),
			card.Card("H", "5"),card.Card("H", "6"),card.Card("H", "7")]
	
	state = State(infos, cards)	
	
	assert not state.isValid()	
	
	#Here one of the community cards is unknown
	player1 = PlayerInfo(0, "John", 0, 100, 10, [card.Card("H", "3"), card.Card("S", "2")], False)			
	player2 = PlayerInfo(1, "Susy", 1, 100, 5, [card.Card("?", "?"), card.Card("?", "?")], False)
	player3 = PlayerInfo(2, "Hamm", 2, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], False)
	player4 = PlayerInfo(3, "Gunn", 3, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], True)
	
	infos = [player1, player2, player3, player4]
	
	cards = [card.Card("H", "A"),card.Card("S", "A"),card.Card("?", "?")]
	
	state = State(infos, cards)	
	
	assert not state.isValid()	
	
	#Here a busted player has pocket cards
	player1 = PlayerInfo(0, "John", 0, 100, 10, [card.Card("H", "3"), card.Card("S", "2")], False)			
	player2 = PlayerInfo(1, "Susy", -1, 0, 0, [card.Card("?", "?"), card.Card("?", "?")], False)
	player3 = PlayerInfo(2, "Hamm", 1, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], False)
	player4 = PlayerInfo(3, "Gunn", 2, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], True)
	
	infos = [player1, player2, player3, player4]
	
	cards = [card.Card("H", "A"),card.Card("S", "A"),card.Card("C", "3")]
	
	state = State(infos, cards)	
	
	assert not state.isValid()	
	
	#Here a busted player has cash
	player1 = PlayerInfo(0, "John", 0, 100, 10, [card.Card("H", "3"), card.Card("S", "2")], False)			
	player2 = PlayerInfo(1, "Susy", -1, 10, 0, [], False)
	player3 = PlayerInfo(2, "Hamm", 1, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], False)
	player4 = PlayerInfo(3, "Gunn", 2, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], True)
	
	infos = [player1, player2, player3, player4]
	
	cards = [card.Card("H", "A"),card.Card("S", "A"),card.Card("C", "3")]
	
	state = State(infos, cards)	
	
	assert not state.isValid()			

	#Here turn orders don't match
	player1 = PlayerInfo(0, "John", 1, 100, 10, [card.Card("H", "3"), card.Card("S", "2")], False)			
	player2 = PlayerInfo(1, "Susy", -1, 0, 0, [], False)
	player3 = PlayerInfo(2, "Hamm", 2, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], False)
	player4 = PlayerInfo(3, "Gunn", 3, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], True)
	
	infos = [player1, player2, player3, player4]
	
	cards = [card.Card("H", "A"),card.Card("S", "A"),card.Card("C", "3")]
	
	state = State(infos, cards)	
	
	assert not state.isValid()	
	
	#Here a busted player is the active player
	player1 = PlayerInfo(0, "John", 0, 100, 10, [card.Card("H", "3"), card.Card("S", "2")], False)			
	player2 = PlayerInfo(1, "Susy", -1, 0, 0, [], True)
	player3 = PlayerInfo(2, "Hamm", 1, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], False)
	player4 = PlayerInfo(3, "Gunn", 2, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], False)
	
	infos = [player1, player2, player3, player4]
	
	cards = [card.Card("H", "A"),card.Card("S", "A"),card.Card("C", "3")]
	
	state = State(infos, cards)	
	
	assert not state.isValid()	
	
	#Here we have more than one active player
	player1 = PlayerInfo(0, "John", 0, 100, 10, [card.Card("H", "3"), card.Card("S", "2")], True)			
	player2 = PlayerInfo(1, "Susy", -1, 0, 0, [], False)
	player3 = PlayerInfo(2, "Hamm", 1, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], True)
	player4 = PlayerInfo(3, "Gunn", 2, 100, 0, [card.Card("?", "?"), card.Card("?", "?")], False)
	
	infos = [player1, player2, player3, player4]
	
	cards = [card.Card("H", "A"),card.Card("S", "A"),card.Card("C", "3")]
	
	state = State(infos, cards)	
	
	assert not state.isValid()	
	
	print "Test successful."