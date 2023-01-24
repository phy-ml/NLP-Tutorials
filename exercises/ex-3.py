# Q: How to tokenize a given text?

from nltk.tokenize import word_tokenize
import spacy

text="Last week, the University of Cambridge shared its own research that shows if everyone wears a mask outside home,dreaded ‘second wave’ of the pandemic can be avoided."

def token_text(text):
    # tokenize with nltk
    nltk_token = word_tokenize(text)

    # tokenize with spacy
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)

    for tok_1, tok_2 in zip(nltk_token, doc):
        print(f'NLTK :{tok_1}  || Spacy :{tok_2.text}')

if __name__ == "__main__":
    token_text(text)