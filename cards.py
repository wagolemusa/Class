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

	#this method drow a specific card randomly
	def drawCard(self):
		return self.cards.pop()

#class for aplayer
class Player(object):
	def __init__(self, name):
		self.name = name
		self.hand = []

	def draw(self, deck):
		self.hand.append(deck.drawCard())
		return self

	#show cards
	def showHand(self):
		for card in self.hand:
			card.show()

	def discard(self):
		return self.hand.pop()

# card = Card("club", 6)
# card.show()

me = Deck()
me.shuffle()

musa = Player("refuge")
musa.draw(me).draw(me)
musa.showHand()

# card = me.drawCard()
# card.show()
# #me.show()
