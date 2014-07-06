#---------------------------------------------------------------------------
#	calculate.py
#
#	Description:
#
#	This is a class for generating tables, probabilities and other data for
#	determining which moves are prudent.
#---------------------------------------------------------------------------

import card, hand, deck

#---------------------------------------------------------------------------
#	comparePockets - This function will, through brute force compare the 
#	hands generated from all possible permutations of cards and return the
#	number (num wins by p1) - (num wins by p2). 
#
#	p1, and p2 should be in the format [Card1a, Card1b], [Card2a, Card2b]
#---------------------------------------------------------------------------
def comparePockets(p1, p2):
	
	d = deck.Deck()
	d.pull(p1[0].suit, p1[0].number)
	d.pull(p1[1].suit, p1[1].number)
	d.pull(p2[0].suit, p2[0].number)
	d.pull(p2[1].suit, p2[1].number)
	assert len(d.cards) == 48
	
	seq = [4, 3, 2, 1, 0]
	numSeq = 1
	score = 0
	handOne = hand.Hand([], 1)
	handTwo = hand.Hand([], 2)
	while True:
		
		communityCards = getComboFromSequence(seq, d.cards)
		handOne.cards = p1 + communityCards
		handTwo.cards = p2 + communityCards
		
		winners = hand.winner([handOne, handTwo])
		if len(winners) == 1:
			if winners[0] == 1:
				score += 1
			else:
				score -= 1
		
		seq = getNextCombinationSequence(seq, d.cards)
		numSeq += 1
		
		if numSeq > 100000:
			numSeq = 0
			print "Another 100000 combinations tested."
		
		if not seq:
			break 
			
	return score
	
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


if __name__ == "__main__":
	
	p1 = [card.Card("H", "3"), card.Card("D", "4")]
	p2 = [card.Card("C", "3"), card.Card("C", "2")]
	
	score = comparePockets(p1, p2)
	
	print "Win percentage = "+ str((1+score/1712304.0)/2)
		
	
	