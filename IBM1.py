'''
This script takes two datasets present in json format.
It translates french to English using IBM Model 1 and EM algorithm
'''

import time
import json
import numpy as np


def IBM1model(file,x=1000):
    #load data from json files
    

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
        
    count = np.zeros(shape=(l1,l2))    # l1xl2 matrix filled with 0s
    total = np.zeros(l1+l2)    #list of size n filled with 0s
    #converged = False
    stotal = np.zeros(l1)
    t = np.zeros(shape=(l1,l2))

    # initialize t(e|f) uniformly
    for i in range(l1):
        for j in range(l2):
            t[i][j] = 1.0/(l1*l2)


   
    while( x ):
        # initialize
    
        #told = t            
        #converged = True    
        
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
                if( 100*abs(t[i][j] -told[i][j])/t[i][j] < 1e-5):
                    converged = False  """
        
                    
        x = x-1
    
    #printData(en_words,fr_words,t)

    return en_words,fr_words,t

# prints matrix consisting of t(e|f) scores
def printData(M):
    #print(s1)
    en_words = M[0]  
    fr_words = M[1]
    t = M[2]         
    s='\t'
    for j in range(len(fr_words)):
        s = s + fr_words[j] + '\t'
    s = s + '\n'
        
    for i in range(len(en_words)):
        s = s + en_words[i] + ' :\t '
        for j in range( len(fr_words)):
            s = s + str(round(t[i][j],3)) + '\t'
        s = s + '\n'
    print(s)
    return

#returns t(e|f) score of a dataset
def tableCheck(M, s_fr, s_en):
    en_words = M[0]
    fr_words = M[1]
    t = M[2]
    e1 = en_words.index(s_en)
    f1 = fr_words.index(s_fr)

    return t[e1][f1]


# IMPORT dataset
file1 = json.load(open('data1.json'))
file2 = json.load(open('data2.json'))
file3 = json.load(open('hamara_corpus.json'))


#get translation probability

M1 = IBM1model(file1,2000)
M2 = IBM1model(file2,1000)
M3 = IBM1model(file3,2000)

#printData(en_word1,fr_word1, t1)  

print(tableCheck(M3,'das','the'))
print(tableCheck(M3,'der','the')) 
printData(M1)
printData(M2)
printData(M3)