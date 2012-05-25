#!/usr/bin/python

from magic_card import *

class deck :
	def __init__( self, name, cards=[] ) :
		self.name = name
		self.cards = cards
	def addCard( self, card ) : 
		self.cards.append(card)
	def getName( self ) :
		return self.name
	def getCards( self ) :
		return self.cards
	def getDeckSize( self ) :
		return len(self.cards)
	def printDeck( self ) :
		for card in self.cards :
			card.printCard()
	#def removeCard( self, card ) : stub for now
			
