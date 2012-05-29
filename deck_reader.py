#!/usr/bin/env python
import os
from random import *
from sys import *
from deck import *
from magic_card import *



class deck_reader :

	def __init__( self ) :
		self.dummy = 0	
	def initRead( self ) :
		inputfile = raw_input('Filepath of deck file: ')
		if os.path.exists(inputfile) == True : deckfile = open(inputfile, 'r')
		else :
			print 'Filepath does not exist'
			sys.exit(1)
		# Create deck
		deck = self.createDeck(deckfile)
#		shuffle(deck.getCards())
#		for card in deck.getCards()[:7] :
#			card.printCard()
		return deck

	def createDeck( self, file ) :
		cards = []
		newdeck = deck(cards)
		# Read the lines from the file and create the cards
		for line in file :
			card_text = line.split(' ')
			newcard = self.makeCard(card_text)
			newdeck.addCard(newcard)
		return newdeck		

		
	def makeCard( self, card_attr ) :
		newcard = magic_card()
		newcard.setType(card_attr[0])
		newcard.setColor(card_attr[1])
		newcard.setMana(card_attr[2])
		newcard.setRarity(card_attr[3])
		# Need to add comment
		for line in card_attr[5:] :
			newcard.appendToComment(line + ' ')
		return newcard		

