import time
import json
import numpy as np
from nltk.translate import IBMModel1, AlignedSent
from nltk.translate import IBMModel2, AlignedSent


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
#ibm2 = IBMModel2(bitext, 2000)
test_sentence = bitext[2]
print(test_sentence.words)
#print('\n')
print(test_sentence.mots)
#print('\n')
print("Alignment according to IBM1 nltk model\n")
print(test_sentence.alignment)

ibm2 = IBMModel2(bitext, 2000)
test_sentence = bitext[2]
print(test_sentence.words)
#print('\n')
print(test_sentence.mots)
#print('\n')
print("Alignment according to IBM2 nltk model\n")
print(test_sentence.alignment)

#print(ibm1.translation_table['der']['the'])
#print(ibm2.translation_table['das']['the'])
'''for i in range(n):
	en_word = en_sentence[i].split(' ')
	for j in range(n):
		fr_word = fr_sentence[j].split(' ')
		print(ibm2.translation_table[fr_word][en_word])
		print('	')
	print('\n')
'''