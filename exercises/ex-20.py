# Q: Find the cosine similarity between two given documents

text1='Taj Mahal is a tourist place in India'
text2='Great Wall of China is a tourist place in china'

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [text1, text2]

vectorize = CountVectorizer()
matrix = vectorize.fit_transform(documents)

# convert matrix into dense matrix
doc_matrix = matrix#.todense()

# compute the cosine similarity
print(f'The cosine similarity is {cosine_similarity(doc_matrix, doc_matrix)}')


