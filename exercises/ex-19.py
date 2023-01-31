# Q: Find the similarity between any two text documents

text1="John lives in Canada"
text2="James lives in America, though he's not from there"

import spacy
nlp = spacy.load('en_core_web_lg')

doc1 = nlp(text1)
doc2 = nlp(text2)

print(f'Similarity between doc1 and doc 2 is {doc1.similarity(doc2)}')