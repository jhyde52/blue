# Path to my nltk data: /Users/jessicahyde/nltk_data
# Command to update/download NLTK data: python -m nltk.downloader
# https://wordnet.princeton.edu/wordnet/documentation/


from nltk.corpus import wordnet as wn
# Commands to see hypernyms of 'panda'
panda = wn.synset('panda.n.01')
hyper = lambda s: s.hypernyms()
list(panda.closure(hyper))


# lemma = lower case ASCII text of word or collocation. Collocations are formed by joining individual words with an underscore (_ ) character.

# lookup of synonyms in wordnet

>>>wn.synsets('blanket')

# [Synset('blanket.n.01'), Synset('blanket.n.02'), Synset('blanket.n.03'), Synset('blanket.v.01'), Synset('blanket.v.02'), Synset('across-the-board.s.01')]


for ss in wn.synsets('small'):
    print(ss)
    for sim in ss.similar_tos():
        print('    {}'.format(sim))
