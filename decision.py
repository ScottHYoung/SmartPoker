#---------------------------------------------------------------------------
#	decision.py
#
#	Description:
#
#	An object that contains a player decision generated by an AI or an
#	interface. All players must pass a decision on each play, however all
#	non-active players can only pass the decision "Wait"
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
#	Decision class
#---------------------------------------------------------------------------

class Decision():
	
	#---------------------------------------------------------------------------
	#	Constructor
	#
	#	Passed a decision name and a value
	#---------------------------------------------------------------------------
	def __init__(self, name = "WAIT", value = 0):
		
		name = name.upper()
		
		assert (name == "WAIT" or 
				name == "FOLD" or
				name == "CHECK" or
				name == "REVEAL" or
				name == "CALL" or
				name == "RAISE" or
				name == "FORFEIT" or
				name == "GAMEQUIT")
		
		self.name = name.upper()
		self.value = value
		
	 