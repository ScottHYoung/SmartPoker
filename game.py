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

import settings, decision, state, card, interface, player, deck, human

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
	def __init__(self, theSettings, theInterfaceConstructor):
		
		self.settings = theSettings
		self.players = []
		
		for i in range(self.settings.numPlayers):
			
			#Make some nicer default names
			if i == 0:
				nameGen = "John"
			elif i == 1:
				nameGen = "Suzy"
			elif i == 2:
				nameGen = "Fred"
			elif i == 3:
				nameGen = "Doug"
			else:
				nameGen = "Player"+str(i)
			
			#Change these to human/AI later
			if i < (self.settings.numPlayers - self.settings.numAIs):
					
				newPlayer = human.Human(theInterfaceConstructor(i), i, nameGen, self.settings.numChips)
			else:
				
				#Currently a Human, replace this with the AI class later
				newPlayer = human.Human(theInterfaceConstructor(i), i, nameGen, self.settings.numChips)
				
			newPlayer.turnOrder = i
			if i == 0:
				newPlayer.isActive = True
				newPlayer.isDealer = True
			self.players.append(newPlayer)
		
		self.smallBlind = self.settings.smallBlind
		self.bigBlind = 2 * self.smallBlind
		self.currentDealer = 0
		self.currentActive = 0
		self.numInGame = self.settings.numPlayers
		self.numInHand = self.settings.numPlayers
		self.communityCards = []
		
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
		self.deck.shuffle()
		
		#Deal the pocket cards
		for player in self.players:
			player.pocket = [self.deck.draw(), self.deck.draw()]
			
			#Do some quick checks to make sure the endHand procedure didn't make any errors
			assert player.pot == 0
			assert player.pocket[0] != None and player.pocket[1] != None
			
		#Subtract the blinds into the pot
		assert self.numInGame >= 2
		
		bigBlinds = 0
		smallBlinds = 0
		
		if self.numInGame == 2:
			#Dealer is small blind, next player is big blind
			
			for player in self.players:
				if player.isDealer:
					if not player.addToPot(self.smallBlind):
						player.addToPot(player.bank)
					smallBlinds += 1
				#Big blind is the other live player
				elif player.turnOrder != -1:
					if not player.addToPot(self.bigBlind):
						player.addToPot(player.bank)
					bigBlinds += 1
						
		else:
			#Dealer position + 1 = SB, Dealer position + 2 = LB
			
			for player in self.players:
				if player.turnOrder == ((self.currentDealer + 1) % self.numInGame):
					if not player.addToPot(self.smallBlind):
						player.addToPot(player.bank)
					smallBlinds += 1
				
				if player.turnOrder == ((self.currentDealer + 2) % self.numInGame):
					if not player.addToPot(self.bigBlind):
						player.addToPot(player.bank)
					bigBlinds += 1
		
		#Make sure we put in the correct amount			
		assert bigBlinds == 1 and smallBlinds == 1
		
		#Set the active player	
		for player in self.players:
			if player.turnOrder == ((self.currentDealer + 3) % self.numInGame):
				player.isActive = True
				self.currentActive = player.turnOrder
			else:
				player.isActive = False				
			
		#Reset the community cards
		self.communityCards = []	
		
		#Betting begins at round 0
		self.bettingRound = 0
		self.numVisitsThisRound = 0
			
		#Start the game
		self.nextAction()
		
	#---------------------------------------------------------------------------
	#	nextAction()
	#
	#	Moves the game to the next point where a decision is needed from the
	#	players.
	#---------------------------------------------------------------------------
	def nextAction(self):
		
		decision = self.passToPlayers()
		
		#Do stuff with that decision
		
	#---------------------------------------------------------------------------
	#	passToPlayers()
	#
	#	Cleans the game states and passes them to each individual player.
	#---------------------------------------------------------------------------	
	def passToPlayers(self):
			
		for givenPlayer in self.players:		

			#Clean game state
			cleanPlayersInfo = []

			for player in self.players:
				info = player.getInfo()
				if not player.hasRevealed and player.id != givenPlayer.id:
					info.pocket = [card.Card("?", "?"), card.Card("?", "?")]
				cleanPlayersInfo.append(info)
			
			gameState = state.State(cleanPlayersInfo, self.communityCards)
			
			decision = givenPlayer.giveDecision(gameState)
			
			if givenPlayer.isActive:
				return decision
			else:
				assert (decision.name == "WAIT"	or decision.name == "FORFEIT" or decision.name == "GAMEQUIT")
				
		#Something went wrong and now we don't have a decision.		
		assert False		
			
			
#========================================
#	TESTS
#========================================	

if __name__ == '__main__':
	
	print "Testing constructor..."
	
	newGame = Game(settings.Settings(), interface.Interface())	
	
	assert len(newGame.players) == 4
	
	for player in newGame.players:
		playerInfo = player.getInfo()
		assert playerInfo.isValid()
	
	print "Test complete."		