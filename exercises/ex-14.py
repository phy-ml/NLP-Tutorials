# Q: Correct the spelling errors in the following text

text="He is a gret person. He beleives in bod"

from textblob import TextBlob

# use the correct function of textblob
text = TextBlob(text)
print(text.correct())
