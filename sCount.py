from __future__ import division

import nltk, re, pprint
from nltk import word_tokenize, bigrams, FreqDist, sent_tokenize
import sys  


reload(sys)  
sys.setdefaultencoding('utf8')

#15 Sentences corpus

f = open('news.txt',"r")
raw = f.read()

tokens = nltk.word_tokenize(raw)
sentences = nltk.sent_tokenize(raw)
taggedWords = nltk.pos_tag(tokens)
count = 0 
for sentence in sentences:
    count = count + 1 
print "There are ", count, " sentences"     # Using the NLP tool to get the amount of sentences

verbCount = 0 
for x in range(len(taggedWords)):
    if taggedWords[x][1].find('VB') != -1:      # Counting only the VBNs that appear in the sentences
        verbCount = verbCount + 1 
print "There are ", verbCount, " verbs"

from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000')

text = "The old oak tree from India fell down."

output = nlp.annotate(text, properties={
  'annotators': 'parse',
  'outputFormat': 'json'
})

print(output['sentences'][0]['parse']) # tagged output sentence

f.close()
