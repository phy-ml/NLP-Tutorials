import os
import re
import string
import random

original_message = '''I then lounged down the street and found,
as I expected, that there was a mews in a lane which runs down
by one wall of the garden. I lent the ostlers a hand in rubbing
down their horses, and received in exchange twopence, a glass of
half-and-half, two fills of shag tobacco, and as much information
as I could desire about Miss Adler, to say nothing of half a dozen
other people in the neighbourhood in whom I was not in the least
interested, but whose biographies I was compelled to listen to.
'''

class EncoderTxt:
    def __init__(self,seed=123):
        # fix the seed for reproducibility
        self.seed = seed

        # build a cypher map
        self.build_cipher_map()

    def build_cipher_map(self):
        # function to build the cypher
        random.seed(self.seed)

        set_1 = list(string.ascii_lowercase)
        set_2 = list(string.ascii_lowercase)
        random.shuffle(set_2)

        self.cipher_map = {set_1[i]:set_2[i] for i in range(len(set_1))}


    def encode(self,text):
        """ method to encode the message using the cipher mapping """
        text = re.sub("[^a-zA-Z]"," ",text)
        text_token = list(text.lower())
        for i in range(len(text)):
            if text_token[i] in self.cipher_map:
                text_token[i] = self.cipher_map[text_token[i]]

        encode_text = ''.join(text_token)
        # print(encode_text)
        return encode_text


    # take the
    def decode(self,encode_msg, mapping):
        """ method to decode the message using the cipher mapping """
        message = list(encode_msg.lower())

        for i in range(len(message)):
            if message[i] in mapping:
                message[i] = mapping[message[i]]

        decode_msg = ''.join(message)
        return decode_msg
def Mapping():
    # get the list of the lower case letters
    letter_1 = list(string.ascii_lowercase)
    letter_2 = list(string.ascii_lowercase)

    # shuffle the letters
    random.shuffle(letter_2)

    # create randomized mapping of letter to letter
    mapping = {}

    for i, j in zip(letter_1, letter_2):
        mapping[i] = j

    return mapping

if __name__ == "__main__":
    print(original_message)
    encoder = EncoderTxt()

    print(encoder.cipher_map)

    # map
    cipher_map = encoder.cipher_map

    encode_msg = encoder.encode(text=original_message)

    decode_msg = encoder.decode(encode_msg=encode_msg,mapping=cipher_map)
    print('Encoded Msg')
    print(encode_msg)

    print('Decode Msg')
    print(decode_msg)

