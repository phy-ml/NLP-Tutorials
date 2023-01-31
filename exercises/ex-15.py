# Q: Clean the following tweet and tokenize them
import tokenize

text=" Having lots of fun #goa #vaction #summervacation. Fancy dinner @Beachbay restro :) "

import re
from nltk.tokenize import TweetTokenizer

# clean the tweet using regex
text = re.sub(r'[^0-9a-zA-Z]+', ' ', text)

# use nltk tweet tokenizer
tokenizer = TweetTokenizer()
print(tokenizer.tokenize(text))