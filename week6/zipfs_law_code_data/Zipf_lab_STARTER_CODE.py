
import sys
import re
import pylab as p
import nltk

nltk.download('brown')

# Import data

from nltk.corpus import brown

# Get a list (strictly, interator-over) all the tokens of the Brown Corpus

brown_words = brown.words()

################################################################

