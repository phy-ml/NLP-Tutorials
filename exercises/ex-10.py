# Q: Perform stemming/ convert each token to it’s root form in the given text

text = "Dancing is an art. Students should be taught dance as a subject in schools . I danced in many of my school function. Some people are always hesitating to dance."


# use nltk for stemming
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

snow = SnowballStemmer(language='english')
stem_text = [snow.stem(token) for token in word_tokenize(text)]
print(" ".join(stem_text))

# spacy does not have a stemmer