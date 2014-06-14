#---------------------------------------------------------------------------
#	game.py
#
#	Description:
#
#	Game manages the rules and procession of the game itself. Initialized with
#	a settings object, the game will then create players and AIs with the 
#	desired settings and start a new hand. The game object will also coordinate 
#	between the player objects sending them states and asking for decisions
#	before proceeding with the next step in the game.
#
#---------------------------------------------------------------------------

import settings, decision, state, card, interface, player, deck

#---------------------------------------------------------------------------
#	Game class
#---------------------------------------------------------------------------
class Game():
	
	#---------------------------------------------------------------------------
	#	Constructor
	#
	#	Passed a settings object the game will initialize the game settings to
	#	begin playing poker.
	#---------------------------------------------------------------------------	
	def __init__(self, theSettings, theInterface):
		
		self.interface = theInterface
		self.settings = theSettings
		
		for i in self.settings.numPlayers:
			
			#Change these to human/AI later
			if i < self.settings.numAIs:
				newPlayer = player.Player(i, "Test"+str(i), self.settings.numChips)
			else:
				newPlayer = player.Player(i, "Test"+str(i), self.settings.numChips)
				
			newPlayer.turnOrder = i
			if i == 0:
				newPlayer.activeTurn = True
				newPlayer.isDealer = True
			self.players.append(newPlayer)
		
		self.smallBlind = self.settings.smallBlind
		self.bigBlind = 2 * self.smallBlind
		self.currentDealer = 0
		self.currentActive = 0
		self.numInGame = self.settings.numPlayers
		self.numInHand = self.settings.numPlayers
		
		self.newHand()
		
	#---------------------------------------------------------------------------
	#	newHand()
	#
	#	Sets the game up for a new hand, making a new deck, dealing the pocket
	#	cards to all players still in the game, subtracting the blinds
	#---------------------------------------------------------------------------
	def newHand(self):
		
		#Make a new deck and shuffle it
		self.deck = deck.Deck()
		self.deck.shuffle
		
		#Deal the pocket cards
		for player in self.players
			player.pocket = [self.deck.draw(), self.deck.draw()]
			
			#Do some quick checks to make sure the endHand procedure didn't make any errors
			assert player.pot == 0
			assert player.pocket[0] != None and player.pocket[1] != None
			
		#Subtract the blinds into the pot
		assert self.numInGame >= 2
		
		if self.numInGame == 2:
			#Dealer is small blind, next player is big blind
			
			#CONTINUE WORKING HERE
			
			pass
		
			
			
			
#========================================
#	TESTS
#========================================	

if __name__ == '__main__':			