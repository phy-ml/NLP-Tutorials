# Q:  Tokenize the given text with stop words (“is”,”the”,”was”) as delimiters.

text = "Walter was feeling anxious. He was diagnosed today. He probably is the best person I know."

stop_word_delimiter = ['is', 'was', 'the', '.', ',', '-', '?', '!']
for i in stop_word_delimiter:
    text = text.replace(i, 'Delim')

words = [i.strip() for i in text.split('Delim')]
words_filter = list(filter(lambda x:x not in [''], words))
print(words_filter)