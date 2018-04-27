#!/bin/bash

# Install nltk
pip install nltk

# Ensure the server is running before opening python
echo "Checking for Stanford Core NLP Server..."
while ! nc -z localhost 9000; do
    echo "Waiting for Stanford Core NLP Server at http://localhost:9000"
    sleep 0.1
done
echo "Done!\n"

# Open and run our script
echo "Writing scores to ../output/results.txt..."
python3 ../src/main.py
echo " Done!"
