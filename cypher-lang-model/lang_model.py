import os
import re
import requests
import numpy as np


original_message = '''I then lounged down the street and found,
as I expected, that there was a mews in a lane which runs down
by one wall of the garden. I lent the ostlers a hand in rubbing
down their horses, and received in exchange twopence, a glass of
half-and-half, two fills of shag tobacco, and as much information
as I could desire about Miss Adler, to say nothing of half a dozen
other people in the neighbourhood in whom I was not in the least
interested, but whose biographies I was compelled to listen to.
'''

class LanguageModel:
    def __init__(self):
        self.train()
        # print(self.markov)
        # print(self.unigram)

    # def __call__(self, *args, **kwargs):
    #     pass

    def update_transition(self, l1, l2):
        # convert the respective letters into ordinal position
        i = ord(l1) - 97
        j = ord(l2) - 97
        self.markov[i,j] += 1

    def update_unigram(self,l):
        # update the unigram
        i = ord(l) - 97
        self.unigram[i] += 1

    def initialize_unigram(self):
        self.unigram = np.zeros(26)

    def initialize_bigram(self):
        self.markov = np.ones((26,26))

    def load_data(self):
        """Load the text data as the corpus"""
        _init_file_dir = os.path.dirname(__file__)
        if os.path.exists(os.path.join(_init_file_dir, "moby_dick.txt")):
            self.corpus = open(os.path.join(_init_file_dir, "moby_dick.txt"), "r")
            # with open(os.path.join(_init_file_dir, "moby_dick.txt"), "r") as file:
            #     self.corpus = file.read()

        # url = "https://lazyprogrammer.me/course_files/moby_dick.txt"
        # response = requests.get(url)
        # self.corpus = response.content.decode("utf-8")


    def train(self):
        # initialize the uni and bigrams
        self.initialize_unigram()
        self.initialize_bigram()

        # load the training data
        self.load_data()

        # # # remove the alpha numeric characters
        # # self.corpus = re.sub("[^a-zA-Z]]", " ", self.corpus)
        # #
        # # # split and convert into lower case
        # # tokens = self.corpus.lower().split()
        regex = re.compile('[^a-zA-Z]')
        for line in self.corpus:
        # for line in open('moby_dick.txt'):
            line = line.rstrip()
            line = regex.sub(' ', line)
            tokens = line.lower().split()

            # update transition probabilities
            for token in tokens:
                # print(token)
                # get the first letter of token
                ch0 = token[0]
                self.update_unigram(token[0])

                # other letters
                for ch1 in token[1:]:
                    self.update_transition(ch0, ch1)
                    # change the c0 val
                    ch0 = ch1

        # get the probabilities
        self.log_markov= np.log(self.markov / self.markov.sum(axis=1, keepdims=True))
        self.log_uni = np.log(self.unigram / self.unigram.sum())

    def word_prob(self, word):
        # get the first word
        i = ord(word[0]) - 97
        log_p = self.log_uni[i]

        # rest of word
        for ch in word[1:]:
            j = ord(ch) - 97
            log_p += self.log_markov[i,j]
            i = j

        return log_p

    def sentence_prob(self, sentence):
        tokens = sentence.split()
        prob = sum([self.word_prob(i) for i in tokens])
        return prob


if __name__ == '__main__':
    LanguageModel()


