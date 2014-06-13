#---------------------------------------------------------------------------
#	smartPoker.py
#
#	Description:
#
#	This is the main file. Run to play.	Make sure you run in the terminal to
#	use the default interface.
#
#	Tested on Python 2.7.5,
#	OSX 10.9.3
#
#	Note: Currently the default interface is written to work only with OSX and
#	possibly Linux running in the terminal.
#---------------------------------------------------------------------------

import os

print "Hello World!"

for z in range(2):
	for i in range(10):
		myText = raw_input()

		print myText
	
	os.system("clear")