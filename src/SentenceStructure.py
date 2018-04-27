import matplotlib.pyplot as plt1
import nltk
import string
import re
import stanfordcorenlp

class SentenceStructure():

    parser = ""

    def __init__(self):
        self.parser = nltk.CoreNLPParser(url="http://localhost:9000")

    # Comb through text and ensure that periods and commas have a space after them.
    def preProcess(self, text):
        text = text.replace(".", ". ")
        text = text.replace(",", ", ")
        text = text.replace(" i ", " I ")
        text = text.replace("  ", " ")
        return text;


    def scoreFormCounts(self,essay):
        formCount = 0
        processedEssay = self.preProcess(essay)
        sawSubject = 0
        sawVerb = 0
        sentences = nltk.sent_tokenize(processedEssay)
        for sentence in sentences:
            sentence = sentence.replace("."," ")        #get different results when i get rid of the period
            try:
                (parse,) = self.parser.raw_parse(sentence)
                parse.pretty_print()
            except:
                parse = ""

            try:
                if parse[0]._label == 'SBAR':           # if the root is an SBAR then it is incomplete
                    print "Found a SBAR",sentence
                    formCount = formCount + 1
            
                elif parse[0]._label == 'FRAG':         # if the root is a fragment it is incomplete
                    print "Found FRAG",sentence
                    formCount = formCount + 1

                elif parse[0]._label == 'PP':           # If the root is a PP, (For the bus all morning)
                    print "Found PP",sentence
                    formCount = formCount + 1

                elif parse[0]._label == 'SINV':
                    formCount = formCount + 1

                subtreeLabels = []
                subtrees = parse.subtrees()
                for subtree in subtrees:
                    subtreeLabels.append(subtree.label())

                labelLength = len(subtreeLabels)
                if subtreeLabels[labelLength-1] in ['CC','IN','DT']:
                    print "Found CC or IN at end"
                    formCount = formCount + 1

                for i in range(labelLength):

                    if subtreeLabels[i] == 'NP':
                        sawSubject = 1

                # if a full stop is followed by a CC or iN then incomplete
                    if subtreeLabels[i] == '.':
                        if subtreeLabels[i-1] in ['CC','IN']:
                            formCount = formCount + 1

                # Had I the wings of a bird
                    if subtreeLabels[i] in ['VBD','VBP','VB','VBZ','VBN','VBG']:
                        sawVerb = 1
                        if sawSubject == 0:
                            print "Got a verb before a subject"
                            formCount = formCount + 1
                if sawVerb == 0:
                    formCount = formCount + 1

            except:
                print "null"
            #print formCount

        return formCount




if __name__ == "__main__":

    # Input a sentence
    #userSentence = raw_input("Enter a sentence: ")

    # Ensure there are spaces between periods and commas. This may not work so well for elipses,
    # But those shouldn't really be in academic writing...
    sentenceForm = SentenceStructure()
    file = "../input/testing/essays/" + "1414676.txt"

    essayFile = open(file, 'r')
    essay = essayFile.read()
    count = sentenceForm.scoreFormCounts(essay)
    #count = sentenceForm.scoreDParser(userSentence)

    #toc = open("../input/testing/index.csv", 'r')

    # Import the table of contents
    #lines = toc.readlines()

    # Skip the title line
    # lines.pop(0)
    # for line in lines:
    #     line = line.split(';')
    #     print(line)
    #     file = "../input/testing/essays/" + line[0]
    #     score = line[2]
    #
    #     if "high" in score:
    #         score = 1
    #     else:
    #         score = 0
    #
    #     essayFile = open(file, 'r')
    #     essay = essayFile.read()
    #
    #     count = sentenceForm.scoreFormCounts(essay)
    #
    #     plt1.scatter(count, score)
    #
    # plt1.show()


    print "Sentence syntax errors",count
    print("Exited")
