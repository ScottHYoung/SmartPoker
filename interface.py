#---------------------------------------------------------------------------
#	interface.py
#
#	Description:
#
#	This is a template for any visualizations for handling the game. All 
#	visualizers must inherit at least these basic methods
#---------------------------------------------------------------------------

import settings, state, decision

#---------------------------------------------------------------------------
#	Interface class
#	
#	Contains three methods: 
#		__init__()
#		setupGame()	- Always uses default settings
#		giveDecision() - Always gives default decision
#---------------------------------------------------------------------------
class Interface():

	#---------------------------------------------------------------------------
	#	Constructor
	#
	#	Does nothing. 
	#---------------------------------------------------------------------------	
	def __init__(self):
		pass

	#---------------------------------------------------------------------------
	#	setupGame()
	#
	#	Returns the default game settings
	#---------------------------------------------------------------------------		
	def setupGame(self):
		
		default = settings.Settings()
		return default

	#---------------------------------------------------------------------------
	#	giveDecision()
	#
	#	Returns the default decision
	#---------------------------------------------------------------------------		
	def giveDecision(self, gameState):
		
		default = decision.Decision()
		return default
		
#========================================
#	TESTS
#========================================	

if __name__ == '__main__':
	
	pass		