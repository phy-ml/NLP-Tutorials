# @: Remove all the stopwords ( ‘a’ , ‘the’, ‘was’…) from the text
import nltk

text="""the outbreak of coronavirus disease 2019 (COVID-19) has created a global health crisis that has had a deep impact on the way we perceive our world and our everyday lives. Not only the rate of contagion and patterns of transmission threatens our sense of agency, but the safety measures put in place to contain the spread of the virus also require social distancing by refraining from doing what is inherently human, which is to find solace in the company of others. Within this context of physical threat, social and physical distancing, as well as public alarm, what has been (and can be) the role of the different mass media channels in our lives on individual, social and societal levels? Mass media have long been recognized as powerful forces shaping how we experience the world and ourselves. This recognition is accompanied by a growing volume of research, that closely follows the footsteps of technological transformations (e.g. radio, movies, television, the internet, mobiles) and the zeitgeist (e.g. cold war, 9/11, climate change) in an attempt to map mass media major impacts on how we perceive ourselves, both as individuals and citizens. Are media (broadcast and digital) still able to convey a sense of unity reaching large audiences, or are messages lost in the noisy crowd of mass self-communication? """

from nltk.corpus import stopwords
import spacy
stop_words = set(stopwords.words('english'))

# tokenize words
tokens = nltk.word_tokenize(text)

new_tokens = []
for i in tokens:
    if i not in stop_words:
        new_tokens.append(i)

print(' '.join(new_tokens))

##################################################

# using spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp(text)

new_token = []
for i in doc:
    if i.is_stop == False:
        new_token.append(i.text)

print(" ".join(new_token))