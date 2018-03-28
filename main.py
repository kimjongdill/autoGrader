import nltk
import string

import nltk.corpus

""" A class for holding word / tag counts for an essay type """

class classStats():

    wordCount = dict()
    bigramCount = dict()

    def __init__(self):
        return;

    def cleanWord(self, word):
        word = word.casefold()

        for c in string.punctuation:
            word = word.replace(c, "")

        return word;

    def addWord(self, word, tag):
        word = self.cleanWord(word)

        if (word, tag) in classStats.wordCount:
            classStats.wordCount[(word, tag)] = classStats.wordCount[(word, tag)] + 1

        else:
            classStats.wordCount[(word, tag)] = 1

        return;

    def printAll(self):
        print(classStats.wordCount)

""" Read the corpus of essays and categorize the words and POS found """

class nGramModel():

    highStats = classStats()
    lowStats = classStats()

    """ Get identifying information from file and load text
        into bigram model"""

    def countbigram(self, line):

        # Open the file and load the essay into memory
        file = open("./essays/" + line[0])
        essay = file.read()

        # Tag the POS
        essay = essay.split()
        tags = nltk.pos_tag(essay)

        # Count the tags
        for tag in tags:
            if "high" in line[2]:
                #print(tag[0] + tag[1])
                nGramModel.highStats.addWord(tag[0], tag[1])

            else :
                print("low")

        nGramModel.highStats.printAll()

        return;


    """Load the training essays"""

    def __init__(self):
        """ Import the table of contents """
        toc = open("./index.csv", 'r')

        # Import the table of contents
        lines = toc.readlines()

        lines.pop(0)

        for line in lines:
            line =  line.split(';')
            self.countbigram(line)

        return;



if __name__ == "__main__":
    print("hello world\n")

    f = nGramModel()