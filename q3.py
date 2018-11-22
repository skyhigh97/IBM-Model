import json
from nltk.translate.phrase_based import phrase_extraction



def extractPhrases(file,alignments):
    i = 0
    print( len(file))
    while i < len(file):
        sourceText = file[i]['en']
        targetText = file[i]['fr']
        # print(sourceText)
        # print(targetText)
        phrases = phrase_extraction(sourceText, targetText, alignments)
        i += 1
        for phrase in phrases:
            phraseList.append((phrase[2], phrase[3]))

def calculateProbabilityScore(phraseList):
    probabilityList = []
    done = set()
    for phrase in phraseList:
        numerator = 0
        denominator = 0
        if tuple((phrase[1], phrase[0])) in done:
            pass
        else:
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


file1 = json.load(open('data1.json'))

alignments = [[(0,0), (1,1), (2,2),(3,3),(4,4)]]
phraseList = []
phraseList = extractPhrases(file1, alignments)
calculateProbabilityScore(phraseList)

