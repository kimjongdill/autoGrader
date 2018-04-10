import nltk
import string
import bigram
import nltk.corpus
from spelling import Spelling


if __name__ == "__main__":
    #f = bigram.nGramModel()

    while 1:

        filename = input("Welcome to the essay scorer. Enter the filename of the essay to score or q to quit: ")

        if filename == "q":
            print("Goodbye")
            break

        try:
            file = open("./essays/"+filename)

        except:
            print(filename + " not found. ")
            continue

        # We can declare classes to run our tests here
        # and then combine the score

        essay = file.read()
        essay = essay.split()
        tags = nltk.pos_tag(essay)


        spell = Spelling()
        print(spell.spellCheck(tags))

        #print(tags)


