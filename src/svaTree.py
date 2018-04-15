import nltk
import string
import re
import stanfordcorenlp

# Reference:
# Yuzhu Wang, Hai Zhao, and Dan Shi. 2015. "A Light Rule-based Approach to English Subject-Verb Agreement Errors
#       on the Third Person Singular Forms." PACLIC 29 345-353

# Identify subject verb agreement
# Identify complete sentences

# Do the writer's full stops correspond with the end of a sentence?
#   - Run-on sentence
#       - Break this into two thoughts?
#   - Incomplete sentence
#       - Try to combine with downstream ideas?
#
# Does the sentence contain a complete subject / object
#   - Forms of Sentences
#   - S -> NP VP        // Declarative
#   - S -> Aux NP VP    // Yes-No Question
#   - S -> WhAux NP VP  // Wh Question
#   - S -> VP           // Command

# Start with just one sentence

class SubjVerbAgreement():

    parser = ""
    svaError = 0
    verbError = 0


    def __init__(self):
        self.parser = nltk.CoreNLPParser(url="http://localhost:9000")
        self.svaError = 0
        self.verbError = 0
        return;

    # Comb through text and ensure that periods and commas have a space after them.
    def preProcess(self, text):
        text = text.replace(".", ". ")
        text = text.replace(",", ", ")
        text = text.replace(" i ", " I ")
        text = text.replace("  ", " ")
        return text;


    def scoreAgreement(self, essay):

        sentenceCount = 0
        errorCount = 0

        cleanEssay = self.preProcess(essay)
        sentences = nltk.sent_tokenize(cleanEssay)


        for sentence in sentences:
            print(sentence)

            sentenceCount += 1
            if not self.decAgreement(sentence):
                errorCount += 1
                print("bad sentence")
            else:
                print("good sentence")

        return float(errorCount / sentenceCount)

    def rec_agreement(self, tree):
        # End recursion at leaf node

        verb = ""
        noun = ""
        errorCount = 0

        if type(tree[0]) is str:
            return 0;


        for node in tree:
            if node._label == "NP":
                noun = self.getNounAgreement(node)

            elif node._label == "VP":
                verb = self.getVerbAgreement(node)

            else:
                self.rec_agreement(node)

        if verb in ["VB", "VBD", "MD"]:
            return;

        if verb == "AM":
            if noun == "I":
                return;

        if verb == "ARE":
            if noun in ["2NN", "2NNS"]:
                return;

        if verb == "VBP":
            if noun in ["2NN", "I"]:
                return;

        if verb == "VBZ":
            if noun == "NN":
                return;

        if noun == "":
            return;

        if verb == "":
            return;

        #tree.pretty_print()
        self.svaError += 1
        return;

    def getNounAgreement(self, tree):

        labels = []
        count = 0

        # Base case - Handle PRPs otherwise return whatever.
        if type(tree[0]) is str:
            word = tree[0].casefold()

            if word == "i":
                return "I"

            if word == "you":
                return "2NN"

            if word in ["we", "they"]:
                return "2NNS"

            if tree._label == "PRP":
                return "NN"

            return tree._label

        for node in tree:
            labels.append(self.getNounAgreement(node))

        if len(labels) == 1:
            return labels[0]

        for label in labels:
            if label in ["NNS", "NNPS"]:
                return "NNS"

            if label in ["NNP", "NN", "I"]:
                count += 1

        if count == 1 and "I" in labels:
            return "I"

        if count == 1:
            return "NN"

        return "NNS"


    def getVerbAgreement(self,tree):

        labels = []
        countError = 0

        if type(tree[0]) is str:
            if tree[0] == "am":
                return "AM"

            if tree[0] == "are":
                return "ARE"

            return tree._label;

        for node in tree:
            if node._label == "S":
                 self.rec_agreement(node)
            else:
                verb = self.getVerbAgreement(node)
                labels.append(verb)

        try:

            if labels[0] == "MD":
                if len(labels) > 1:
                    if labels[1] in ["VBZ", "VBP", "AM", "VBD"]:
                        self.verbError += 1
                        return labels[1]


            """if len(labels) > 1:
                if labels[1] == "VBN":
                    if not labels[0] in ["VBZ", "VBP", "AM", "VBD"]:
                        print("Error - bad past participal")
                        return [labels[0], countError + 1]
            """

            return labels[0]

        except:

            return ""

    def treeAgreement(self, essay):

        sentenceCount = 0
        errorCount = 0

        # Ensure that punctuation has proper spacing
        cleanEssay = self.preProcess(essay)
        sentences = nltk.sent_tokenize(cleanEssay)

        for sentence in sentences:
            print(sentence)
            (parse, ) = self.parser.raw_parse(sentence)
            # Now we have a parse tree. We can check subject verb agreement for
            # Every S->NP VP in the tree.
            parse.pretty_print()
            self.rec_agreement(parse)
            print("svaError: ", self.svaError)
            print("verbError: ", self.verbError)

        return errorCount


if __name__ == "__main__":

    # Input a sentence
    userSentence = input("Enter a sentence: ")

    # Ensure there are spaces between periods and commas. This may not work so well for elipses,
    # But those shouldn't really be in academic writing...

    sva = SubjVerbAgreement()
    print("Errors: ", sva.treeAgreement(userSentence))
    #sva.scoreAgreement(userSentence)
    print("goodbye")




