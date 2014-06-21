Project start date: June 12th, 2014

Currently a work in progress, my goal is to make an extremely stripped down 
interface for playing Texas Hold'em, a program for running the game and a
computer AI which can make decisions based on beliefs about the unknown cards
and likelihood of success at each point in the game.

I'm not entirely sure how well this will turn out, but anyone is free to watch
the progress!

To Do:

- Get rid of turnOrder (replace with id and isInGame, isInHand)
- Finish nextAction() function:
	- Process actions
		- Check (nothing)
		- Call (xfer money)
		- Raise (xfer money)
		- Fold (switch to !isInHand)
		- Forfeit (switch to !isInGame & !isInHand)
	- Determine if hand is still going, and if not, redistribute pots to winner and endHand()
	- Increment active player
	- Determine if betting round has ended, and nextBettingRound()
	
- Add AI class