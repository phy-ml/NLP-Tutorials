# Q: Import spacy and load the language model

import spacy
nlp = spacy.load("en_core_web_sm")
print(nlp)