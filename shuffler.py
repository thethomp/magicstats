#!/usr/bin/python

import os
from operator import itemgetter
from time import localtime, strftime
from random import *
from sys import *
from deck import *
from magic_card import *



class shuffler :

	def __init__( self, deck) :
		self.deck = deck
		self.num_shuffles = 1
		self.lands = 0
		self.creatures = 0
		self.spells = 0
		self.mana_str = 'Mana Cost '


	def sortedDictValues( self, adict ):	
		items = adict.items()
		items.sort()
		return [value for key, value in items]
	
	
	def create_deck_dict( self, deck ) :
		deck_dict = {}
		deck_dict_index = 0
		for card in deck.getCards() :
			if card.getType() not in deck_dict :
				deck_dict[card.getType()] = 0
				deck_dict_index += 1
			if card.getColor() not in deck_dict :
				deck_dict[card.getColor()] = 0
				deck_dict_index += 1
			if (self.mana_str + str(card.getMana())) not in deck_dict :
				deck_dict[self.mana_str + str(card.getMana())] = 0
				deck_dict_index += 1
			if card.getRarity() not in deck_dict :
				deck_dict[card.getRarity()] = 0
				deck_dict_index += 1


		return deck_dict


	def shuffle_deck( self, deck, log=True, shuff_num=1, deal_num=1 ) :
		total = self.create_deck_dict( deck )
		
		if log :
			logfile = open('goblin_deck_' + strftime("%a-%d-%b-%Y-%H:%M:%S", localtime()) + '.log', 'w')
			
		orig_deck_array = deck.getCards()	

		for num in range(0, deal_num):
			local = self.create_deck_dict( deck )
			#logfile.write('Hand #' + str(num+1) + '\n\n')
			temp_deck = orig_deck_array
			for num in range(0, shuff_num) :
				shuffle(temp_deck)
			 	
			# Print results to std out
			for card in temp_deck[:7] :
				local[card.getType()] += 1  # get the cards type
				total[card.getType()] += 1
				local[card.getColor()] += 1  # get the cards color
				total[card.getColor()] += 1
				local[self.mana_str + card.getMana()] += 1  # get the cards mana cost
				total[self.mana_str + card.getMana()] += 1
				local[card.getRarity()] += 1  # get the cards rarity
				total[card.getRarity()] += 1
			#	if log :
			#		logfile.write(card.saveString())
			#logfile.write('\n')
			#for k, v in local.iteritems() : 
			#	logfile.write('Total ' + k + ' in hand = ' + str(v) +'\n') 

#			logfile.write('\n---------------------------------------\n\n')
		
		logfile.write('\n================ Stats ===================\n\n')
		logfile.write('Total hands = ' + str(deal_num) + '\t\t\n')
		logfile.write('Total shuffles per hand = ' + str(shuff_num) + '\n\n')
		# Print totals
		sorted_total = sorted(total.items(), key=itemgetter(1))
		for sub in sorted_total :
			total_str = ("Total %s = " % (sub[0]))
			width = 30 - len(total_str)
			logfile.write( ("%s%s\n" % (total_str, str(sub[1]).rjust(width))) )
		logfile.write('\n')
		# Print averages
		for sub in sorted_total :
			avg_str = ("Average %s = " % (sub[0]))
			width = 30 - len(avg_str)
			logfile.write(("%s%s\n" % (avg_str, str(round(float(float(sub[1])/float(deal_num)),2)).rjust(width))))
#			logfile.write('Avg ' + k + ' per hand = ' + str(float( float(v)/float(deal_num) )) + '\n')
		
		logfile.close()	






	
