import nltk


import nltk.corpus

class nGramModel():
    highBigrams = []
    lowBigrams = []


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
                print("high")

            else :
                print("low")

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