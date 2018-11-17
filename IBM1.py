'''
This script takes two datasets present in json format.
It translates french to English using IBM Model 1 and EM algorithm
'''

import time
import json
import numpy as np

#load data from json files
file1 = json.load(open('data1.json'))
file2 = json.load(open('data2.json'))

#to store sentences
fr_sentence = []
en_sentence = []

#to store all  words
fr_words = []
en_words = []

#to store translation probability
#t = {}

#append each sentence into lists
for i in range(len(file1)):    
    fr_sentence.append(file1[i]['fr'])
    en_sentence.append(file1[i]['en'])
    
for i in range(len(file2)):    
    fr_sentence.append(file2[i]['fr'])
    en_sentence.append(file2[i]['en'])    


n = len(en_sentence)
  
#store all words in sets 
for i in range(n):                 
    en_word = en_sentence[i].split(' ')
    
    for tmp in en_word:
        if(not(tmp in en_words)):
            en_words.append(tmp)
    
    fr_word = fr_sentence[i].split(' ')
    
    for tmp in fr_word:
        if(not(tmp in fr_words)):
            fr_words.append(tmp)
           
    

            
l1 = len(en_words)
l2 = len(fr_words)

#print(en_words)
#print(fr_words)
    
count = np.zeros(shape=(l1,l2))    # nxn matrix filled with 0s
total = np.zeros(l1+l2)    #list of size n filled with 0s
converged = None
stotal = np.zeros(l1+l2)
t = np.zeros(shape=(l1,l2))

# initialize t(e|f) uniformly
for i in range(l1):
    for j in range(l2):
        t[i][j] = np.random.uniform(0,1)

'''
s='\t'
for j in range(l2):
    s = s + fr_words[j] + '\t'
s = s + '\n'
    
for i in range(l1):
    s = s + en_words[i] + ' :\t '
    for j in range(l2):
        s = s + str(round(t[i][j],2)) + '\t'
    s = s + '\n'
print(s)'''
    
x = 2000    
        
while( x ):
    # initialize
   
        
    converged = True    
    
    for i in range(n):
        #compute normalization
        e =  en_sentence[i].split(' ')
        f =  fr_sentence[i].split(' ')
        
        for en_word in e :
            e1 = en_words.index(en_word)
            stotal[e1] = 0
            
            for fr_word in f :
                f1 = fr_words.index(fr_word)
                stotal[e1] +=  t[e1][f1]
        
        # collect counts
        for en_word in e :
            for fr_word in f :
                e1 = en_words.index(en_word)
                f1 = fr_words.index(fr_word)
                
                count[e1][f1] += t[e1][f1]/stotal[e1]
                total[f1] += t[e1][f1]/stotal[e1]
    
    #estimate probabilities
    for fr_word in fr_words:
        for en_word in en_words:
            e1 = en_words.index(en_word)
            f1 = fr_words.index(fr_word)
            t[e1][f1] = count[e1][f1]/total[f1]
            
    #check for convergence
    """
    for i in range(l1):
        for j in range(l2):
            if( t[i][j] > 0.05 and  t[i][j] < 0.95):
                converged = False  """
                
    x = x-1

#print(s1)
                
s='\t'
for j in range(l2):
    s = s + fr_words[j] + '\t'
s = s + '\n'
    
for i in range(l1):
    s = s + en_words[i] + ' :\t '
    for j in range(l2):
        s = s + str(round(t[i][j],2)) + '\t'
    s = s + '\n'
print(s)
    

      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        