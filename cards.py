import random
class Cards(object):
	def __init__(self, suit, val):
		self.suit = suit
		self.value = val

	#display cards
	def show(self):
		print '{} of {}'.format(self.value, self.suit)


class Deck(object):
	def __init__(self):
		self.cards = []
		self.build()

	def	build(self):
		for s in ["kamuli", "supedi", "mutima", "Dai"]:
			for v in range(1, 14):
				self.cards.append(Cards(s, v))

	def show(self):
		for c in self.cards:
			c.show()
		
	# shuffle is in build method to display random cards	
	def shuffle(self):
		for i in range(len(self.cards)-1, 0, -1):
			r = random.randint(0,i)
			self.cards[i], self.cards[r] = self.cards[r], self.cards[i]


# card = Card("club", 6)

# card.show()

me = Deck()
me.shuffle()
me.show()
