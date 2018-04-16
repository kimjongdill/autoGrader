#!/bin/bash

# Install nltk
pip install nltk

# Startup stanford coreNLP server
cd ../src/stanford-corenlp-full-2018-02-27

nohup java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000 &

# Ensure the server is running before opening python
while ! nc -z localhost 9000; do
    sleep 0.1
done

# Navigate back to execution folder
cd ..
cd ../executable

# Open and run our script
python3 ../src/main.py

# On exit close the server
