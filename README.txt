Project start date: June 12th, 2014

Currently a work in progress, my goal is to make an extremely stripped down 
interface for playing Texas Hold'em, a program for running the game and a
computer AI which can make decisions based on beliefs about the unknown cards
and likelihood of success at each point in the game.

I'm not entirely sure how well this will turn out, but anyone is free to watch
the progress!

To Do:

- Create Game test suite
- Add reveal code to endHand (add new game variable lastRaised, force that person to reveal first)
- Add code for split pots
- Add code for ties
- Add code for winning the game
- Make hand.winner() work properly
- Don't allow player to raise when all they can do is call
- Make "C" key work for both calling and checking since they are mutually exclusive actions
	
- Add AI class