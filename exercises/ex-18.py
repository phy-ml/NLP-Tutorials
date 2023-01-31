# Q: Find the similarity between any two words.

word1="amazing"
word2="terrible"
word3="excellent"

import spacy
nlp = spacy.load('en_core_web_lg')

# create tokens
token_1 = nlp(word1)
token_2 = nlp(word2)
token_3 = nlp(word3)

# print the similarity
print(f'Similarity between {word1} and {word2} is {token_1.similarity(token_2)}')
print(f'Similarity between {word2} and {word3} is {token_2.similarity(token_3)}')
print(f'Similarity between {word1} and {word3} is {token_1.similarity(token_3)}')