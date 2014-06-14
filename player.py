#---------------------------------------------------------------------------
#	player.py
#
#	Description:
#
#	Player is a template class that has a getDecision function which, in the
#	case of a human player, is passed directly to the interface, and in the
#	case of an AI player, the AI will calculate a decision.
#
#	The player also contains a number of attributes throughout the game and
#	can yield those as a playerInfo object via getInfo()
#
#---------------------------------------------------------------------------

import decision

#---------------------------------------------------------------------------
#	Player class
#---------------------------------------------------------------------------
class Player():

	#---------------------------------------------------------------------------
	#	Constructor
	#---------------------------------------------------------------------------
	def __init__(self, ID, name, bank):
		
		self.id = ID
		self.name = name
		self.bank = chips
		
		self.pot = 0
		self.turnOrder = -1
		self.isDealer = False
		self.pocket = []
		self.activeTurn = False	
		self.miscInfo = []
		
	#---------------------------------------------------------------------------
	#	getInfo()
	#
	#	Returns a set of player info for use in the game state
	#---------------------------------------------------------------------------
	def getInfo(self):
		
		return PlayerInfo(self.id, self.name, self.turnOrder, self.bank, self.pot, self.pocket, self.activeTurn, self.miscInfo)

	#---------------------------------------------------------------------------
	#	giveDecision(state)
	#
	#	Given a game state, returns the decision of the player
	#---------------------------------------------------------------------------	
	def giveDecision(self, state):
		
		default = decision.Decision()
		return default
		
#---------------------------------------------------------------------------
#	PlayerInfo class
#
#	Holds all info per player in the game necessary for the interface & any
#	decisions.
#---------------------------------------------------------------------------		
class PlayerInfo():
	
	#---------------------------------------------------------------------------
	#	Constructor
	#
	#	Takes an ID, name, turn order, bank, pot contribution, pocket cards, activeTurn
	#	and miscInfo string array
	#---------------------------------------------------------------------------
	def __init__(self, ID, name, turnOrder, bank, pot, pocket, isDealer, activeTurn, miscInfo = []):
		
		self.id = ID
		self.name = name
		self.turnOrder = turnOrder
		self.bank = bank
		self.pot = pot
		self.pocket = pocket
		self.isDealer = isDealer
		self.activeTurn = activeTurn
		self.miscInfo = miscInfo
		
	#---------------------------------------------------------------------------
	#	isValid()
	#
	#	Determines whether player info is valid
	#---------------------------------------------------------------------------	
	def isValid(self):
		
		if self.turnOrder < -1:
			return False
			
		if self.turnOrder == -1:
			if self.bank > 0:
				return False
			if self.pot > 0:
				return False
			if self.activeTurn:
				return False
			if self.isDealer:
				return False
			if len(self.pocket) > 0:
				return False
		else:
			if self.bank == 0 and self.pot == 0:
				return False
			if len(self.pocket) != 2:
				return False
			elif not self.pocket[0].isValid() or not self.pocket[1].isValid():
				return False
		
		if self.bank < 0:
			return False
			
		if self.pot < 0:
			return False
			
		#All tests are passed
		return True
		
#========================================
#	TESTS
#========================================	
if __name__ == '__main__':	
	pass	