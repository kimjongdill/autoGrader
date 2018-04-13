#import sys
#sys.path.insert(0, '../src')
from src.spelling import Spelling
from src.subjectVerbAgreement import SubjVerbAgreement

if __name__ == "__main__":
    #f = bigram.nGramModel()

    while 1:

        filename = input("Welcome to the essay scorer. Enter the filename of the essay to score or q to quit: ")

        if filename == "q":
            print("Goodbye")
            break

        try:
            file = open("./input/testing/essays/"+filename)

        except:
            print(filename + " not found. ")
            continue

        # We can declare classes to run our tests here
        # and then combine the score

        # Read the essay from file, let testers tokenize as necessary.
        essay = file.read()

        spell = Spelling()
        sva = SubjVerbAgreement()

        print("Spelling score (0-4): " + str(spell.spellCheck(essay)))
        print("Grammar score (5-0): " + str(sva.scoreAgreement(essay)))


        #print(tags)


