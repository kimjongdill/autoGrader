import nltk
from nltk.corpus import words
import string

#print(words.words())

class Spelling():
    numErrors = 0
    dictionary = dict()

    """ Check for punctuation """
    def isPunct(self, c):
        if c in string.punctuation:
            return True;

        return False;

    # Put corpus in hash map to speed up search
    def __init__(self):
        for word in words.words():
            self.dictionary[word] = True

    """ Checking spelling """
    def spellCheck(self, text):
        self.numErrors = 0
        for pair in text:
            # Split the word / tag pair
            word = pair[0]
            tag = pair[1]
            wList = []

            # Clean word for the dictionary
            if tag is not "NNP":
                word = word.casefold()

            # Remove trailing punctuation
            while(self.isPunct(word[len(word)-1])):
                word = word[:-1]

            wList.append(word)
            # Split word by internal punctuation
            for i in range(0, len(word)):
                if self.isPunct(word[i]):
                    wList.pop()
                    wList.append(word[:i])
                    wList.append(word[i+1:])

            # Look for word in dictionary
            for word in wList:
                if word not in self.dictionary:
                    # Handle regular plurals and 'ed' endings
                    if len(word) > 1 and (word[len(word)-1] == "s" or word[len(word)-1] == "d"):
                        word = word[:-1]
                        if word in self.dictionary:
                            continue

                    print(word)
                    self.numErrors += 1