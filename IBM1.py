'''
This script takes two datasets present in json format.
It translates french to English using IBM Model 1 and EM algorithm
'''

import math
import json



file1 = json.load(open('data1.json'))
file2 = json.load(open('data1.json'))

#to store sentences
fr_sentence = []
en_sentence = []

#append each sentence into lists
for i in range(len(file1)):    
    fr_sentence.append(file1[i]['fr'])
    en_sentence.append(file1[i]['en'])
for i in range(len(file2)):    
    fr_sentence.append(file2[i]['fr'])
    en_sentence.append(file2[i]['en'])    

s = ''
for i in range(len(en_sentence)): 
    s = s + fr_sentence[i] + ' : ' + en_sentence[i]+'\n'
    
print(s)   
