#---------------------------------------------------------------------------
#	AI_random.py
#
#	Description:
#
#	AI_random is a player class which does nothing but picks moves totally
#	at random, irrespective of actual cards being held.
#
#---------------------------------------------------------------------------

import random
import player, interface, state

#---------------------------------------------------------------------------
# AI_random class
#---------------------------------------------------------------------------
class AI_Random(player.Player):
	
	#---------------------------------------------------------------------------
	# Constructor
	# 
	# Takes an id, name and bank value
	#---------------------------------------------------------------------------
	def __init__(self, ID, name, bank):
		
		player.Player.__init__(self, ID, name, bank)
		self.interface = interface	
		
	#---------------------------------------------------------------------------
	#  giveDecision()
	# 
	#  Selects a decision at random from the available options
	#---------------------------------------------------------------------------
	def giveDecision(self, theState):	
		
		decisions = theState.decisionOptions()
		
		choice = random.randint(0,100)
		theDecision = None
		#Generally folding, checking or revealing should always be an option
		for d in decisions:
			if d.name == decision.Decision.FOLD or d.name == decision.Decision.CHECK or d.name == decision.Decision.REVEAL:
				theDecision = d
				
		#Sanity test that we could have checked, folded or revealed		
		assert theDecision != None
				
		for d in decisions:
			if d.name == decision.Decision.CALL and choice > 50:
				theDecision = d
			if d.name == decision.Decision.RAISE and choice > 85:
				for p in theState.playersInfo:
					if p.id = self.id:
						me = p
				
				possibleRaise = me.bank - theState.getCallAmount()
				myRaise = possibleRaise
				if possibleRaise > 0:
					if choice > 96: #go all-in
						myRaise = possibleRaise
					elif choice > 90: #big raise
						myRaise = int(me.bank/4) 
						if myRaise > possibleRaise:
							myRaise = possibleRaise
					else:	#small raise
						myRaise = int(me.bank/8)
						if myRaise > possibleRaise:
							myRaise = possibleRaise
							
				theDecision = decision.Decision(decision.Decision.RAISE, myRaise)
				
		return theDecision
				
			
		

#========================================
#	TESTS
#========================================
if __name__ == '__main__':

	ai = AI_Random(3, "John", 100)