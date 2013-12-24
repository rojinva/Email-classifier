
__author__="rojin.varghese"
__date__ ="$Nov 29, 2013 7:29:16 PM$"


import os

word_freq = {}

def parse(line):
  text = line
  BAD_CHARS = ".!?,\'\">*-"

  words = [ word.strip(BAD_CHARS) for word in text.strip().split() if len(word) > 3 ]
  word_freq = {}
  for word in words :
    word_freq[word] = word_freq.get(word, 0) + 1

  tx = [ (v, k) for (k, v) in word_freq.items()]
  tx.sort(reverse=True)
  word_freq_sorted = [ (k, v) for (v, k) in tx ]
  print(word_freq_sorted)
  term_importance = lambda word : 1.0/word_freq[word]
  print map(term_importance, word_freq.keys())


for root, dirs, files in os.walk("C:/Documents and Settings/rojin.varghese/Desktop/Keyword_extraction"):
    for file in files:
        if file.endswith(".txt"):
             a = os.path.join(root, file)
             text_file = open( a , "r")
             lines = text_file.read()
             parse(lines)
             text_file.close()

             
