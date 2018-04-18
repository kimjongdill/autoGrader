import sys
sys.path.insert(0, './')
from spelling import Spelling
from subjectVerbAgreement import SubjVerbAgreement as sva
from sCount import SentenceCount
from svaTree import SubjVerbAgreement
from FeatureAnalysis import FeatureAnalysis

if __name__ == "__main__":
    #f = bigram.nGramModel()

    # Import the table of contents
    toc = open("../input/testing/index.csv", 'r')

    resultsFile = open("../output/results.txt", 'w')

    # Import the table of contents
    lines = toc.readlines()

    # Skip the title line
    lines.pop(0)

    for line in lines:
        line = line.split(';')
        filename = line[0]

        try:
            file = open("../input/testing/essays/"+filename)

        except:
            print(filename + " not found. ")
            continue

        # We can declare classes to run our tests here
        # and then combine the score

        # Read the essay from file, let testers tokenize as necessary.
        essay = file.read()

        spell = Spelling()
        stc = SentenceCount()
        feat = FeatureAnalysis()

        spellingScore = str(spell.spellCheck(essay))
        sentenceScore = stc.scoreSentenceCount(essay)

        verbScores = feat.analyze(essay)
        svaScore = verbScores[0]
        verbScore = verbScores[1]




        reportString = filename + ";" + str(spellingScore) + ";" + str(sentenceScore) + ";" + str(svaScore) + ";" + \
                       str(verbScore) + ";0;0;0;0;unknown\n"

        resultsFile.write(reportString)
        resultsFile.flush()
        print(reportString)

        # print("Spelling score (0-4): " + str(spell.spellCheck(essay)))
        # print("Sentence Count: ", stc.scoreSentenceCount(essay))
        # print("Bad SVA Count: ", feat.analyze(essay))
        # # print("Grammar score (5-0): " + str(sva.scoreAgreement(essay)))


        #print(tags)
    resultsFile.close()


