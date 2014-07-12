#---------------------------------------------------------------------------
#	calculate.py
#
#	Description:
#
#	This is a class for generating tables, probabilities and other data for
#	determining which moves are prudent.
#---------------------------------------------------------------------------

from math import factorial
import card, hand, deck

#---------------------------------------------------------------------------
#	comparePocketsFast - This function will, compare two pockets using an
#	optimized method of calculation to be faster, but still return an
#	identical result to comparePockets()
#
#	p1, and p2 should be in the format [Card1a, Card1b], [Card2a, Card2b]
#---------------------------------------------------------------------------
def comparePocketsFast(p1, p2, c = []):
	
	pass

#---------------------------------------------------------------------------
#	comparePockets - This function will, through brute force compare the 
#	hands generated from all possible permutations of cards and return the
#	number of wins, ties and losses out of a total of 1712304 possibilities
#
#	p1, and p2 should be in the format [Card1a, Card1b], [Card2a, Card2b]
#	optionally can pass a set of community cards to fix.
#---------------------------------------------------------------------------
def comparePockets(p1, p2, c = []):
	
	d = deck.Deck()
	d.pull(p1[0].suit, p1[0].number)
	d.pull(p1[1].suit, p1[1].number)
	d.pull(p2[0].suit, p2[0].number)
	d.pull(p2[1].suit, p2[1].number)
	for ci in c:
		d.pull(ci.suit, ci.number)
		
	assert len(d.cards) == 48 - len(c)
	
	seq = [4, 3, 2, 1, 0]
	seq = seq[len(c):]
	numSeq = 1
	wins = 0
	ties = 0
	losses = 0
	handOne = hand.Hand([], 1)
	handTwo = hand.Hand([], 2)
	while True:
		
		communityCards = getComboFromSequence(seq, d.cards) + c
		handOne.cards = p1 + communityCards
		handTwo.cards = p2 + communityCards
		
		winners = hand.winner([handOne, handTwo])
		if len(winners) == 1:
			if winners[0] == 1:
				wins += 1
			else:
				losses += 1
		else:
			ties += 1
		
		seq = getNextCombinationSequence(seq, d.cards)
		numSeq += 1
		
		if numSeq > 100000:
			numSeq = 0
			print "Another 100000 combinations tested."
		
		if not seq:
			break 
			
	return (wins, ties, losses)
	
#---------------------------------------------------------------------------
#	getNextCombinationSequence(seq, l)
#
#	Pulls the next combination from a list, given a sequence array which
#	stores which elements are being pulled and a list to choose from
#
#	Algorithm:
#
#	Sequence looks like [last, 2nd last, 3rd last, etc.]
#
#	Bump the first sequence index. If you can't, bump the second and
#	put the first sequence index back to one spot ahead of it. If you can't
#	bump the third and put the 2nd and first right after, etc.
#	Only when we can't bump any do we return False
#---------------------------------------------------------------------------	
def getNextCombinationSequence(seq, l):
	
	for bump in range(len(seq)):
		
		#If we can bump this up more
		if seq[bump] < len(l)-(bump+1):
			seq[bump] += 1
			#Reset the previous sequence spots
			for reset in range(bump):
				seq[reset] = seq[bump]+(bump-reset)
				
			return seq
			
	return False
	
#---------------------------------------------------------------------------
#	getComboFromSequence(seq, l)
#	
#	Gets the actual combination given an array of indices
#---------------------------------------------------------------------------	
def getComboFromSequence(seq, l):
	
	combo = []
	for s in seq:
		combo.append(l[s])
		
	return combo
	
#---------------------------------------------------------------------------
#	choose(n, r)
#	
#	Returns nCr = n! / ((n-r)! * r!)
#---------------------------------------------------------------------------
def choose(n, r):
	
	assert n >= r
	
	if n == r:
		return 1
	
	#First, make r equal to whichever is higher r-n or r, since the calculation
	#will be equivalent but we'll have smaller intermediate numbers
	if r < n-r:
		r = n-r
		
	#Now compute n! / r! 
	num = 1
	for i in range(r+1, n+1):
		num *= i
	
	#Now divide by (n-r)!
	den = 1
	for i in range(1, n-r+1):
		den *= i
	
	return num/den
	


if __name__ == "__main__":
	
	p1 = [card.Card("H", "A"), card.Card("D", "2")]
	p2 = [card.Card("C", "K"), card.Card("C", "Q")]
	c = [card.Card("C", "A")]
	
	numPossibilities = choose(48-len(c), 5-len(c)) 
	
	wins, ties, losses = comparePockets(p1, p2, c)
	
	print "Win percentage = "+ str(100.0*wins/numPossibilities)+"%"
	print "Tie percentage = "+ str(100.0*ties/numPossibilities)+"%"
	print "Loss percentage = "+ str(100.0*losses/numPossibilities)+"%"
		
	
	