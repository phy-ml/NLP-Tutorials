# @: Remove all the punctuations in the given text

text="The match has concluded !!! India has won the match . Will we fin the finals too ? !"

import string
import nltk
import spacy

# using spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
spacy_token = []

for token in doc:
    if token.is_punct == False:
        spacy_token.append(token.text)

print(" ".join(spacy_token))

# use NLTK
tokenizer = nltk.RegexpTokenizer(r"\w+")
nltk_token = []
for token in tokenizer.tokenize(text):
    nltk_token.append(token)
print(" ".join(nltk_token))


# use normal procedure
tokenizer = nltk.word_tokenize(text)
normal_token = []

for token in tokenizer:
    if str(token) not in string.punctuation:
        normal_token.append(token)

print(" ".join(normal_token))
