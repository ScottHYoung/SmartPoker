#---------------------------------------------------------------------------
#	basicInterface.py
#
#	Description:
#
#	This is an extremely basic terminal-based interface which displays the
#	player's cards, community cards and opponents. It refreshes itself each
#	time the player requires a decision.
#---------------------------------------------------------------------------

import os, interface, state, decision, settings

#---------------------------------------------------------------------------
# basicInterface
#---------------------------------------------------------------------------
class BasicInterface(interface.Interface):
	
	
	#---------------------------------------------------------------------------
	#	Constructor
	#---------------------------------------------------------------------------
	def __init__(self, playerID = -1):
		
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
		

		for playersInfo in theState.playersInfo:
			if playersInfo.id == self.id:
			
				thisPlayerInfo = playersInfo
			
				if playersInfo.isActive == False:
					#-------AUTO PUSH "WAIT" FOR INACTIVE PLAYERS-------
					#
					#---------------------------------------------------
					return(decision.Decision("WAIT"))
					#---------------------------------------------------
					#
					#---------------------------------------------------
		
		#First clear the screen - TURNED OFF
		os.system("clear")
		
		#Now display the game state
		self.drawState(theState)
		
		#Now get the user prompt
		theDecision = decision.Decision("WAIT")
		
		print " "
		print "Your options:"
		
		while True:
			
			#Now display the user options
			decisions = theState.decisionOptions(self.id)
			for d in decisions:
				
				callAmount = theState.getCallAmount(thisPlayerInfo)
				if d.name == "CALL":
					dText = d.name + " (" + str(callAmount) + ")"
				elif d.name == "RAISE" and callAmount > 0:
					dText = "RAISE (+" + str(callAmount) + " TO CALL)"
				else:
					dText = d.name
				print dText	
				
		
			print " "
			
			rawText = raw_input()
			
			splitText = rawText.split()
			
			decisionText = splitText[0].upper()
			
			if len(splitText) > 1:
				try:
					decisionValue = int(splitText[1])
				except ValueError:
					decisionValue = 0
			else:
				decisionValue = 0
			
			if decisionText == "W" or decisionText == "WAIT":
				theDecision = decision.Decision("WAIT")
			elif decisionText == "F" or decisionText == "FOLD":
				theDecision = decision.Decision("FOLD")	
			elif decisionText == "C" or decisionText == "CHECK":
				theDecision = decision.Decision("CHECK")			
			elif decisionText == "R" or decisionText == "RAISE":
				theDecision = decision.Decision("RAISE", decisionValue)
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
			communityStr += self.cardString(commCard) + " "
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
				
			playerStr += " " 
			
			if p.isInGame:	
				playerStr += p.name
				
				playerStr += "\t\t"
				
				playerStr += self.cardString(p.pocket[0])+" "+self.cardString(p.pocket[1])
			
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
				