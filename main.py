import nltk


import nltk.corpus

class nGramModel():
    highBigrams = []
    lowBigrams = []


    """ Get identifying information from file and load text
        into bigram model"""

    def countbigram(self, line):
        line = line.split(';')
        file = open("./essays/" + line[0])
        essay = file.read()
        print(essay)
        return;

    """Load the training essays"""
    def __init__(self):
        """ Import the table of contents """
        toc = open("./index.csv", 'r')

        # Import the table of contents
        lines = toc.readlines()

        lines.pop(0)

        for line in lines:
            self.countbigram(line)

        return;



if __name__ == "__main__":
    print("hello world\n")

    f = nGramModel()