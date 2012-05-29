magicstats
==========

Command line application to compute useful statistics about any given Magic the Gathering deck. Simply make a .deck file to represent your deck, and magicstats does the rest!

usage: magicstats.py [-h] [-f DECKFILE] [-s SHUFFLE_NUM] [-d DEAL_NUM]

Run the MagicStats deck analysis program.

optional arguments:
  -h, --help            show this help message and exit
  -f DECKFILE, --file DECKFILE
                        Input .deck format file
  -s SHUFFLE_NUM, --shuffle SHUFFLE_NUM
                        Number of times the deck should be shuffled before
                        being delt (default=1)
  -d DEAL_NUM, --deal DEAL_NUM
                        Number of hands to deal (default=1)
