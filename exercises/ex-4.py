# Q: How to get the sentences of a text document ?

text="""The outbreak of coronavirus disease 2019 (COVID-19) has created a global health crisis that has had a deep impact on the way we perceive our world and our everyday lives. Not only the rate of contagion and patterns of transmission threatens our sense of agency, but the safety measures put in place to contain the spread of the virus also require social distancing by refraining from doing what is inherently human, which is to find solace in the company of others. Within this context of physical threat, social and physical distancing, as well as public alarm, what has been (and can be) the role of the different mass media channels in our lives on individual, social and societal levels? Mass media have long been recognized as powerful forces shaping how we experience the world and ourselves. This recognition is accompanied by a growing volume of research, that closely follows the footsteps of technological transformations (e.g. radio, movies, television, the internet, mobiles) and the zeitgeist (e.g. cold war, 9/11, climate change) in an attempt to map mass media major impacts on how we perceive ourselves, both as individuals and citizens. Are media (broadcast and digital) still able to convey a sense of unity reaching large audiences, or are messages lost in the noisy crowd of mass self-communication? """

import nltk
from nltk.tokenize import sent_tokenize
import spacy

def print_sentence(text):
    # tokenize a sentence using NLTk
    print('Tokenize sentence using NLTK')
    sent_tok = sent_tokenize(text)
    for tok in sent_tok:
        print(tok)

    print('--'*20)

    print('Tokenize sentence using spacy')
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)

    for tok in doc.sents:
        print(tok)

if __name__ == "__main__":
    print_sentence(text)