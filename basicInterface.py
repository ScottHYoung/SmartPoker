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
				

	#---------------------------------------------------------------------------
	#	drawState()
	#
	#	Draws the game board and the state for all of the players
	#---------------------------------------------------------------------------		