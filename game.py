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

import settings, decision, state, card, interface, player, deck, human, hand

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
				
			if i == 0:
				newPlayer.isActive = True
				newPlayer.isDealer = True
			self.players.append(newPlayer)
		
		self.smallBlind = self.settings.smallBlind
		self.bigBlind = 2 * self.smallBlind
		self.currentDealer = 0
		self.currentActive = 0
		self.bettingRound = 0
		self.numVisits = 0
		self.numInGame = self.settings.numPlayers
		self.numInHand = self.settings.numPlayers
		self.communityCards = []
		self.numPlayers = self.settings.numPlayers
		
		gameOver = False
		while not gameOver:
			gameOver = self.newHand()
		
	#---------------------------------------------------------------------------
	#	newHand()
	#
	#	Sets the game up for a new hand, making a new deck, dealing the pocket
	#	cards to all players still in the game, subtracting the blinds
	#---------------------------------------------------------------------------
	def newHand(self):
		
		#Check that the game hasn't ended
		if self.numInGame <= 1:
			return True
		
		#Put everyone still playing back in the hand
		for p in self.players:
			if p.isInGame:
				p.isInHand = True
		self.numInHand = self.numInGame
		
		#Make a new deck and shuffle it
		self.deck = deck.Deck()
		self.deck.shuffle()
		
		#Deal the pocket cards
		for player in self.players:
			player.pocket = [self.deck.draw(), self.deck.draw()]
			
			#Do some quick checks to make sure the endHand procedure didn't make any errors
			assert player.pot == 0
			assert player.pocket[0] != None and player.pocket[1] != None
		
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
				elif player.isInGame:
					if not player.addToPot(self.bigBlind):
						player.addToPot(player.bank)
					bigBlinds += 1
						
		else:
			#Dealer position + 1 = SB, Dealer position + 2 = LB
			
			for player in self.players:
				if player.id == ((self.currentDealer + 1) % self.numPlayers):
					if not player.addToPot(self.smallBlind):
						player.addToPot(player.bank)
					smallBlinds += 1
				
				if player.id == ((self.currentDealer + 2) % self.numPlayers):
					if not player.addToPot(self.bigBlind):
						player.addToPot(player.bank)
					bigBlinds += 1
		
		#Make sure we put in the correct amount			
		assert bigBlinds == 1 and smallBlinds == 1
		
		#Set the active player	
		for player in self.players:
			if player.id == ((self.currentDealer + 3) % self.numInGame):
				player.isActive = True
				self.currentActive = player.id
			else:
				player.isActive = False				
			
		#Reset the community cards
		self.communityCards = []	
		
		#Betting begins at round 0
		self.bettingRound = 0
		self.numVisits = 1
			
		#Start the game
		handOver = False
		while not handOver:
			handOver = self.nextAction()
			
		return False
		
	#---------------------------------------------------------------------------
	#	nextAction()
	#
	#	Moves the game to the next point where a decision is needed from the
	#	players.
	#---------------------------------------------------------------------------
	def nextAction(self):
		
		theDecision = self.passToPlayers()
		
		activePlayer = self.getActivePlayer()
		
		checkIfHandOver = False
		
		if theDecision.name == "GAMEQUIT":
			raise SystemExit
			
		elif theDecision.name == "FORFEIT":
			activePlayer.bank = 0
			self.removeFromGame(activePlayer)
			checkIfHandOver = True
			
		elif theDecision.name == "FOLD":
			self.removeFromHand(activePlayer)
			checkIfHandOver = True
		
		elif theDecision.name == "CHECK":
			pass
			
		elif theDecision.name == "CALL":
			amountToCall = self.getCallAmount(activePlayer)
			if not activePlayer.addToPot(amountToCall):
				activePlayer.addToPot(activePlayer.bank)
				
		elif theDecision.name == "RAISE":
			amountToCall = self.getCallAmount(activePlayer)
			amountToRaise = theDecision.value
			if not activePlayer.addToPot(amountToCall + amountToRaise):
				#Checks should have been in place to ensure we can't raise more than we have
				assert False
				
		else:
			
			#Currently we shouldn't be able to do any other actions
			assert False
			
		if checkIfHandOver:
			numInHand = 0
			for p in self.players:
				if p.isInHand:
					numInHand += 1
			
			if numInHand <= 1:
				
				self.endHand()
				
				
				return True
		
		
		
		newBettingRound = self.incrementActivePlayer()
		
		handOver = False
		if newBettingRound:
			
			handOver = self.newBettingRound()	
			
		return handOver
			
	#---------------------------------------------------------------------------
	#	incrementActivePlayer()
	#
	#	Moves to the next active player in sequence, increments the number of
	#	visits and compares whether a full loop in the betting has finished.
	#	Returns true if the betting round has finished.
	#---------------------------------------------------------------------------		
	def incrementActivePlayer(self):
		
		p = self.getPlayerByID(self.currentActive)
		p.isActive = False
		
		while True:
			
			self.numVisits += 1
			self.currentActive = (self.currentActive + 1) % self.numPlayers
			
			p = self.getPlayerByID(self.currentActive)
			
			assert p != None
			
			if p.isInHand == True:
				break
				
		p.isActive = True
		
		# Check if there are unresolved raises that other players must respond to
		uncheckedBets = False
		for p2 in self.players:
			callAmount = self.getCallAmount(p2)
			if p2.isInHand and callAmount > 0:
				uncheckedBets = True
				
		# If we've been once around and there are no unchecked raises, the betting round is over		
		if self.numVisits > self.numPlayers and uncheckedBets == False:
			return True
		else:
			return False
		
	#---------------------------------------------------------------------------
	#	newBettingRound()
	#
	#	Resets the numVisits, increments the bettingRound, changes to the correct
	#	active player, deals any community cards and/or ends the hand
	#---------------------------------------------------------------------------		
	def newBettingRound(self):

		self.numVisits = 1
		self.bettingRound += 1
		
		if self.bettingRound <= 3:
		
			p = self.getPlayerByID(self.currentActive)
			p.isActive = False
			
			self.currentActive = (self.currentDealer + 1) % self.numPlayers
	
			while True:
		
				self.currentActive = (self.currentActive + 1) % self.numPlayers
			
				p = self.getPlayerByID(self.currentActive)
			
				assert p != None
			
				if p.isInHand == True:
					break
				
			p.isActive = True
		
			#Run specific betting round
		
			if self.bettingRound == 1:
			
				#The Flop
				self.communityCards.append(self.deck.draw())
				self.communityCards.append(self.deck.draw())
				self.communityCards.append(self.deck.draw())
			
			elif self.bettingRound == 2:
			
				#The Turn
				self.communityCards.append(self.deck.draw())
			
			elif self.bettingRound == 3:
			
				#The River
				self.communityCards.append(self.deck.draw())
		
		# We've reached the end of all betting
		else:
			self.endHand()
			return True
			
		return False
			
	#---------------------------------------------------------------------------
	#	endHand()
	#
	#	Check if there is only one player left inHand, in which case, give him
	#	the pot and call a new hand. If there is more than one, reveal the cards
	#	of those remaining and calculate the winner
	#---------------------------------------------------------------------------
	def endHand(self):
		
		theWinner = None
		
		thePot = 0
		for p in self.players:
			thePot += p.pot
			p.pot = 0
			
		if self.numInHand == 1:
			for p in self.players:
				if p.isInHand:
					theWinner = p
					
		elif self.numInHand > 1:
			
			#NEED TO ADD REVEAL CODE HERE
			
			assert len(self.communityCards) == 5
			
			hands = []
			for p in self.players:
				if p.isInHand:
					hands.append(hand.Hand(p.pocket + self.communityCards, ID = p.id))
					
			winningID = hand.winner(hands)
					
			theWinner = self.getPlayerByID(winningID)		
							
				
			
		else:
			assert False
			
		theWinner.bank += thePot
		
		#Increment the dealer
		
		p = self.getPlayerByID(self.currentDealer)
		p.isDealer = False
		while True:
	
			self.currentDealer = (self.currentDealer + 1) % self.numPlayers
		
			p = self.getPlayerByID(self.currentDealer)
		
			assert p != None
		
			if p.isInGame == True:
				break
			
		p.isDealer = True		
			
		
	#---------------------------------------------------------------------------
	#	removeFromHand()
	#
	#	Takes the player out of the hand
	#---------------------------------------------------------------------------	
	def removeFromHand(self, thePlayer):
		thePlayer.isInHand = False
		self.numInHand -= 1	
		
	#---------------------------------------------------------------------------
	#	removeFromGame()
	#
	#	Takes the player out of the hand and the game
	#---------------------------------------------------------------------------	
	def removeFromGame(self, thePlayer):
		thePlayer.isInHand = False
		self.numInHand -= 1	
		thePlayer.isInGame = False
		self.numInGame -= 1			
		
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
		
	#---------------------------------------------------------------------------
	#	getActivePlayer()
	#
	#	Returns the active player
	#---------------------------------------------------------------------------				
	def getActivePlayer(self):
		numActive = 0
		activePlayer = None
		for player in self.players:
			if player.isActive:
				activePlayer = player
				numActive += 1
		assert numActive == 1
		return activePlayer
		
	#---------------------------------------------------------------------------
	#	getCallAmount()
	#
	#	Returns the amount in the pot that has not been called by the player
	#---------------------------------------------------------------------------		
	def getCallAmount(self, player):
		maxPot = 0
		for p in self.players:
			if p.pot > maxPot:
				maxPot = p.pot
		
		return maxPot - player.pot
		
	#---------------------------------------------------------------------------
	#	getPlayerByID(id)
	#
	#	Returns the player with the specified ID
	#---------------------------------------------------------------------------
	def getPlayerByID(self, ID):
		for p in self.players:
			if p.id == ID:
				return p		
		return None
			
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