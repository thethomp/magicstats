#!/usr/bin/python

# This class describes the Python MagicCard
# object and all its attributes.

class magic_card :
# Initializer for the MagicCard object
	def __init__( self, type='None', color='Colorless', mana_cost=0, rarity='C', comment=''): 
		self.type = type
		self.color = color
		self.cost = mana_cost
		self.rarity = rarity
		self.comment = comment
	def setType( self, new_type ) :
		self.type = new_type
	def getType( self ) :
		return self.type
	def setColor( self, new_color ) :
		self.color = new_color
	def getColor( self ) :
		return self.color
	def setMana( self, new_mana ) :
		self.cost = new_mana
	def getMana( self ) :
		return self.cost
	def appendToComment( self, new_comment ) :
		self.comment += new_comment
	def getComment( self ) :
		return comment
	def setRarity( self, new_rarity ) :
		self.rarity = new_rarity
	def getRarity( self ) :
		return self.rarity
	def printCard( self ) :
		print 'Type: ' + self.type
		print 'Color: ' + self.color
		print 'Mana cost: ' + self.cost
		print 'Rarity: ' + self.rarity
		print 'Comment: ' + self.comment
		print '\n' 
	def saveString( self ) :
		return self.type + ' ' + self.color + ' ' + str(self.cost) + ' ' + self.rarity + ' ' + 'comment ' + self.comment 
