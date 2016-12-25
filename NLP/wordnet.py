# Path to my nltk data: /Users/jessicahyde/nltk_data
# Command to update/download NLTK data: python -m nltk.downloader

# Commands to see hypernyms of 'panda'
from nltk.corpus import wordnet as wn
panda = wn.synset('panda.n.01')
hyper = lambda s: s.hypernyms()
list(panda.closure(hyper))