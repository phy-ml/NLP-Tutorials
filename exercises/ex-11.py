# Q: Perform lemmatzation on the given text

text = "Dancing is an art. Students should be taught dance as a subject in schools . I danced in many of my school function. Some people are always hesitating to dance."

# use nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk_lemma = WordNetLemmatizer()
nltk_token = [nltk_lemma.lemmatize(token) for token in word_tokenize(text)]
print(" ".join(nltk_token))

# use spacy
import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(text)

spacy_lemma = [token.lemma_ for token in doc]
print(" ".join(spacy_lemma))
