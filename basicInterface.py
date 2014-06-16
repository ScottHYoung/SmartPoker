#---------------------------------------------------------------------------
#	basicInterface.py
#
#	Description:
#
#	This is an extremely basic terminal-based interface which displays the
#	player's cards, community cards and opponents. It refreshes itself each
#	time the player requires a decision.
#---------------------------------------------------------------------------

import os, interface, state, decision

#---------------------------------------------------------------------------
# basicInterface
#---------------------------------------------------------------------------
class BasicInterface(interface.Interface):
	
	
	#---------------------------------------------------------------------------
	#	Constructor
	#---------------------------------------------------------------------------
	def __init__(self, playerID):
		
		interface.Interface.__init__(self)
		self.id = playerID

	#---------------------------------------------------------------------------
	#	setupGame()
	#
	#	For now, just start with the initial game settings
	#---------------------------------------------------------------------------		
	def setupGame(self):

		default = settings.Settings()
		return default
		

	#---------------------------------------------------------------------------
	#	getDecision()
	#---------------------------------------------------------------------------
	def getDecision(self, theState):
		
		#First clear the screen
		os.system("clear")
		
		#Now display the game state
		self.drawState(theState)
		
		#Now get the user prompt
		theDecision = decision.Decision("WAIT")
		while True:
			
			#Now display the user options
			decisions = theState.getDecisionOptions(self.id)
			for d in decisions:
				print d.name			
			
			decisionText = raw_input()
			
			decisionText = decisionText.upper()
			
			if decisionText == "W" or decisionText == "WAIT":
				theDecision = decision.Decision("WAIT")
			elif decisionText == "F" or decisionText == "FOLD":
				theDecision = decision.Decision("FOLD")	
			elif decisionText == "C" or decisionText == "CHECK":
				theDecision = decision.Decision("CHECK")			
			elif decisionText == "R" or decisionText == "RAISE":
				theDecision = decision.Decision("RAISE")
				# EXPAND THIS TO GRAB VALUE
			elif decisionText == "REVEAL":
				theDecision = decision.Decision("REVEAL")
			elif decisionText == "FORFEIT":
				theDecision = decision.Decision("FORFEIT")
			elif decisionText == "CALL":
				theDecision = decision.Decision("CALL")
			elif decisionText == "GAMEQUIT" or decisionText == "QUIT":
				theDecision = decision.Decision("GAMEQUIT")
								
			if theState.isValidDecision(self.id, theDecision):
				break
			else:
				print "Sorry, you can't do that right now."
				
		return theDecision		

	#---------------------------------------------------------------------------
	#	drawState()
	#
	#	Draws the game board and the state for all of the players
	#---------------------------------------------------------------------------	
	def drawState(self, theState):
		
		communityStr = "Community cards: "
		for commCard in theState.communityCards:
			communityStr += self.cardStr(commCard) + " "
		print communityStr
		
		for p in theState.playersInfo:
			
			playerStr = ""
			
			if p.isActive:
				playerStr += "*"
			else:
				playerStr += " "
			
			if p.isDealer:
				playerStr += "D"
			else:
				playerStr += " "
			
			if p.turnOrder >= 0:	
				playerStr += p.name
			
				playerStr += "\t\t"
				playerStr += str(p.bank)
			
				playerStr += "\t\t"
				if p.pot > 0:
					playerStr += "IN: "+str(p.pot)
			else:
				playerStr += "("+p.name+")"
				
			print playerStr
			
			
		
	#---------------------------------------------------------------------------
	#	drawCard()
	#
	#	Draws an individual card
	#---------------------------------------------------------------------------
	def cardString(self, theCard):
		
		assert theCard.isValid()
		
		cardStr = ""
		
		if theCard.suit == "hearts":
			cardStr += "H"
		elif theCard.suit == "diamonds":
			cardStr += "D"
		elif theCard.suit == "clubs":
			cardStr += "C"
		elif theCard.suit == "spades":
			cardStr += "S"
		elif theCard.suit == "unknown":
			cardStr += "?"
			
		if theCard.number == "unknown":
			cardStr += "?"
		else:
			cardStr += theCard.number
			
		return cardStr
				