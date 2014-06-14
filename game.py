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

import settings, decision, state, card, interface, player

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
			self.players.append(newPlayer)