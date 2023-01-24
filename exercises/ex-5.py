# Q: How to tokenize a text using the `transformers` package ?

text="I love spring season. I go hiking with my friends"

from transformers import AutoTokenizer

# initizlize a tokenizer
token = AutoTokenizer.from_pretrained('bert-base-uncased')

# encode the text with tokenizer
inputs = token.encode(text)
print(inputs)

# decode the token back into text
print(token.decode(inputs))