import time
import json
import numpy as np
from nltk.translate import IBMModel1, AlignedSent


#load data from json files
file = json.load(open('hamara_corpus.json'))

#to store sentences
fr_sentence = []
en_sentence = []

#to store all  words
fr_words = []
en_words = []

#to store translation probability

#append each sentence into lists
for i in range(len(file)):    
    fr_sentence.append(file[i]['fr'])
    en_sentence.append(file[i]['en'])
    

n = len(en_sentence)

bitext = []

#store all words in sets 

for i in range(n):                 
    en_word = en_sentence[i].split(' ')    
    fr_word = fr_sentence[i].split(' ')    
    bitext.append(AlignedSent(fr_word, en_word))

ibm1 = IBMModel1(bitext, 2000)

print(ibm1.translation_table['das']['the'])
print(ibm1.translation_table['der']['the'])

