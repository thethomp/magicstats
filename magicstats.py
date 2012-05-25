#!/usr/bin/python

##############################################
#
#
#                   MAGIC
#                   STATS
#
#
#                  *THOMP*
#
#
#
################################################

import sys
import argparse
import deck_builder
import deck_reader
import deck
import magic_card
import shuffler

# Parse command line arguments
parser = argparse.ArgumentParser(description='Run the MagicStats deck analysis program.')
parser.add_argument('-f', '--file', type=argparse.FileType('r'), action='store', dest='deckfile', help='Input .deck format file')

parser.add_argument('-s', '--shuffle', type=int, action='store', dest='shuffle_num', help='Number of times the deck should be shuffled before being delt (default=1)', default=1)
parser.add_argument('-d', '--deal', type=int, action='store', dest='deal_num', help='Number of hands to deal (default=1)', default=1)

try:
	args = parser.parse_args() 
except IOError: 
	print 'ERROR: Could not open input deck file'
	sys.exit(1)


shuffle_num = int(args.shuffle_num)
deal_num = int(args.deal_num)
deckfile = args.deckfile


# Create deck
reader = deck_reader.deck_reader()
deck = reader.createDeck(deckfile)

##in_deck = reader.initRead()
shuff = shuffler.shuffler(deck)

# retrieve how many time the deck should be shuffled
shuff.shuffle_deck(deck, True, shuffle_num, deal_num)


