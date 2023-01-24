# @: Add the custom stopwords “NIL” and “JUNK” in spaCy and remove the stopwords in below text

text=" Jonas was a JUNK great guy NIL Adam was evil NIL Martha JUNK was more of a fool "

import spacy
nlp = spacy.load('en_core_web_sm')

# add custom stop words
custom_stop = ['NIL', 'JUNK']
for i in custom_stop:
    nlp.vocab[i].is_stop = True

doc = nlp(text)

token = [i.text for i in doc if not i.is_stop]

print(" ".join(token))