import time
import json
import numpy as np
from nltk.translate import IBMModel1, AlignedSent


#load data from json files
def IBM1_IBM2(filename):
	file = json.load(open(filename))
    #print("Corpus:"filename)

	#to store sentences
	fr_sentence = []
	en_sentence = []

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
	for i in range(n) :
		test_sentence = bitext[i]
		print(test_sentence.words)
		print(test_sentence.mots)
		print("Alignment according to IBM1 nltk model :")
		print(test_sentence.alignment)
		print('\n\n')
        
    
	ibm2 = IBMModel2(bitext, 2000)
	
	for i in range(n):
		test_sentence = bitext[i]
		print(test_sentence.words)
		#print('\n')
		print(test_sentence.mots)
		#print('\n')
		print("Alignment according to IBM2 nltk model : ")
		print(test_sentence.alignment)
		print('\n\n')
    

print("Corpus: own_corpus" )
IBM1_IBM2('new_corpus.json')
print("Corpus: data1")
IBM1_IBM2('data1.json')
print("Corpus: data2")
IBM1_IBM2('data2_.json')

#print(ibm1.translation_table['der']['the'])
#print(ibm2.translation_table['das']['the'])
