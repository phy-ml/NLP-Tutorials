# Q: Extract and print all the nouns present in the below text

text="James works at Microsoft. She lives in manchester and likes to play the flute"

import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(text)

for token in doc:
    if token.pos_ == "NOUN" or token.pos_ == "PROPN":
        print(token.text)