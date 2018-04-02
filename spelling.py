import nltk
from nltk.corpus import words
#from nltk.corpus import wordnet as wn
from nltk.stem.snowball import SnowballStemmer
import string

#print(words.words())

class Spelling():
    numErrors = 0
    dictionary = dict()
    stemmer = SnowballStemmer("english")

    """ Check for punctuation """
    def isPunct(self, c):
        if c in string.punctuation:
            return True;

        return False;

    # Put corpus in hash map to speed up search
    def __init__(self):
        for word in words.words():
            self.dictionary[word] = True

    def doubleConsonant(self, word):
        if word[-1] == word[-2]:
            newWord = word[:-2]
            if newWord in self.dictionary:
                return newWord
        return word;

    """ Strip ed, s endings"""
    def stripEnding(self, word):

        # Deal with Gerund *ing
        if "ing" in word[-3:]:
            word = word[:-3]
            word = self.doubleConsonant(word)
            if word not in self.dictionary:
                word = word + "e"

        # Plural ies
        elif "ies" in word[-3:] or "ied" in word[-3:]:
            word = word[:-3] + "y"

        # Plural "ren" as in children
        elif "ren" in word[-3:]:
            word = word[:-3]

        # Plural s
        elif "s" in word[-1:]:
            word = word[:-1];

        # Past tense "ed"
        elif "ed" in word[-2:]:
            word = word[:-2];
            word = self.doubleConsonant(word)
            if word not in self.dictionary:
                word = word + "e"

        # Past participle "n"
        elif "n" in word[-1:]:
            word = word[:-1]

        # Adjective "ier"
        elif "ier" in word[-3:]:
            word = word[:-3]
            word += "y"

        # Adjective "er"
        elif "er" in word[-2:]:
            word = word[:-2]


        return word;

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
            while(self.isPunct(word[len(word)-1]) and len(word) > 1):
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

                # Skip if word is whitespace
                if word.isspace() or len(word) == 0:
                    continue

                if word not in self.dictionary:
                    # Handle regular plurals and 'ed' endings
                    newWord = self.stripEnding(word)

                    # Stem word and see if its root is in the dictionary
                    # newWord = self.stemmer.stem(word)
                    if newWord in self.dictionary:
                        continue

                    print(word)
                    self.numErrors += 1

            """
            # Look for word in wordNet
            if not wn.synset(word):
                print(word)
                self.numErrors += 1
            """