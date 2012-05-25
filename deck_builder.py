#!/usr/bin/python

import sys
from magic_card import *
from deck import *

class deck_builder :


	def __init__( self ) :
		self.dummy = 0			

# Function to create a card, it prompts the user
# for each attribute and adds it to the card
# accordingly.
	def createCard( self, deck ) :
		# Create new card
		newcard = magic_card()
		# Get attribute info about the card
		type = raw_input('Enter type: ')
		newcard.setType(type)
		color = raw_input('Enter color: ')
		newcard.setColor(color)
		cost = raw_input('Enter mana cost (integer): ')
		newcard.setMana(cost)
		rarity = raw_input('Enter rarity: ')
		newcard.setRarity(rarity)
		comment	= raw_input('Enter comment (optional): ')
		newcard.appendToComment(comment)
		howmany = raw_input('How many of this card would you like to add to ' + deck.getName() + ': ' )
		# To make sure the input is a number, if not, it's default is 1
		try:
    			howmany = int(howmany)
		except ValueError:
    			howmany = 1
		# Add the specified number of cards to the deck	for i in range(0,howmany) :
			deck.addCard(newcard)
		# Return the deck with the new card(s) added
		return deck		 

# This function takes in a deck object and writes it to 
# a file, using the name of the deck plus '.deck'
# The file is formatted according to the saveString function
# located in the magic_card.py file
	def saveDeck( self, deck ) :
		newname = deck.getName().replace(' ', '_')
		output = file( newname + '.deck', 'w')
		for card in deck.getCards() :
			output.write(card.saveString())	

# Main thread of execution

	def initDeck( self ) :
		create = raw_input('Create new deck? (y or n): ')
		if create == 'n' : sys.exit(0) 
		deck_name = raw_input('Enter Name of Deck: ')
		list = []
		gamedeck = deck(deck_name, list)
		# Loop to create cards to add to the deck
		while True:
			newcard = raw_input('Create a card? (y or n): ')
			if newcard == 'n' : break
			if newcard == 'y' : gamedeck = self.createCard( gamedeck )
		# Check to see the user wants to save the deck
		while True:
			save = raw_input('Would you like to save this deck (y or n): ')
			if save == 'n' : break
			if save == 'y' :
				self.saveDeck(gamedeck)
				print 'Save successful!'
				break






