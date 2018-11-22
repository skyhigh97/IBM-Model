import json
from nltk.translate.phrase_based import phrase_extraction

def extractPhrases(file,alignments):
    i = 0
    phraseList = []
    
    while i < len(file):
        sourceText = file[i]['en']
        targetText = file[i]['fr']
        # print(sourceText)
        # print(targetText)
        phrases = phrase_extraction(sourceText, targetText, alignments)
        i += 1
        for phrase in phrases:
            phraseList.append((phrase[2], phrase[3]))
            
    return phraseList

def calculateProbabilityScore(phraseList):
    probabilityList = []
    done = set()
    for phrase in phraseList:
        numerator = 0
        denominator = 0
        if not (tuple((phrase[1], phrase[0])) in done):
            for tup in phraseList:
                if tup[0] == phrase[0]:
                    denominator += 1
                    if tup[1] == phrase[1]:
                        numerator += 1
            probability = numerator*1.0/denominator
            done.add(tuple((phrase[1], phrase[0])))
            probabilityList.append((phrase[1], phrase[0], probability))


    for i in sorted(probabilityList, key = lambda x: (-x[2],x[1])):
        print((i[1], i[0], i[2]))
    
    print('\n\n')
    return

file2 = json.load(open('data2_.json'))
file3 = json.load(open('new_corpus.json'))

alignments2 = [ (0, 0) ,(1, 1) ,(2, 2) ,(3, 3) ,(4, 4) ,(4, 5) ,(5, 6) ,(6, 7) ,(7, 8) ,(8, 9) ,(9, 10) ,(10, 11) ,(3, 12) ]
alignments3 = [ (0, 0) ,(1, 1) ,(2, 2) ,(5, 3) ,(3, 4) ,(4, 5) ,(6, 6) ,(2, 7) ,(3, 8) ,(8, 9) ,(8, 10) ,(2, 11) ,(7, 12) ,(9, 13) ,(11, 14) ,(11, 15)]
phraseList2 = []
phraseList3 = []
phraseList2 = extractPhrases(file2, alignments2)
phraseList3 = extractPhrases(file3, alignments3)
calculateProbabilityScore(phraseList2)
calculateProbabilityScore(phraseList3)


