import numpy as np
import random
import string
from lang_model import *
from mapping import *
from copy import copy

class GA:
    """Naive Implementation of genetic algorithm"""
    POOL_SIZE = 20
    OFFSPRING_POOL_SIZE = 5
    NUM_ITER = 301

    def __init__(self):
        # initialize the dna pool
        self._init_dnal_pool()

        # initialize encoder
        self._init_encoder()

        # initialize the language model
        self._init_lang_model()

    def _init_dnal_pool(self):
        """generate a DNA Pool"""
        # get a list of all the letter in alphabet
        self.all_letter = list(string.ascii_lowercase)

        # generate 20 random permutation of the letetrs as dna pool
        self.dna_pool = [ "".join(list(np.random.permutation(self.all_letter))) for _ in range(self.POOL_SIZE)]

        self.offspring_pool = []

    def _init_lang_model(self):
        """Initialize the language model"""
        self.language_model = LanguageModel()

    def _init_encoder(self):
        """Initialize the encode module"""
        self.encoder = EncoderTxt()

    @staticmethod
    def random_swap(sequence):
        """swap two characters at random position"""

        # generate two random index
        index_1, index_2 = random.sample(list(np.arange(len(sequence))), 2)

        # swap positions
        sequence_copy = copy(sequence)
        seq_list = list(sequence_copy)
        seq_list[index_1], seq_list[index_2] = seq_list[index_2], seq_list[index_1]
        return "".join(seq_list)

    def evolve_offspring(self):
        """Evolve offspring by random swap for every dna sequence in the dna pool"""

        for dna in self.dna_pool:
            # evolve 10 offspring for each dna in the dna pool
            self.offspring_pool += [self.random_swap(dna) for _ in range(self.OFFSPRING_POOL_SIZE)]

        return self.offspring_pool + self.dna_pool

    def train(self,initial_msg):
        """Train the GA by the real data from the initial message"""

        # initialize the vars
        self.avg_scores_per_iter = np.zeros(self.NUM_ITER)
        self.best_scores_per_iter = np.zeros(self.NUM_ITER)
        self.best_dna = None
        self.best_mapping = None
        self.best_score = float("-inf")
        dna_scores = {}

        # get encoded message from initial message
        encoded_msg = self.encoder.encode(initial_msg)

        # iterate
        for i in range(self.NUM_ITER):
            #only evolve offspring on the second iteration onwards
            if i >0:
                self.dna_pool = self.evolve_offspring()

            # find scores for each dna
            for dna in self.dna_pool:
                curr_mapping = {
                    original_letter:encoded_letter
                    for original_letter, encoded_letter
                    in zip(self.all_letter, dna)}

                # decode using current mapping and get score
                curr_decoded_msg = self.encoder.decode(encode_msg=encoded_msg, mapping=curr_mapping)

                dna_scores[dna] = self.language_model.sentence_prob(sentence=curr_decoded_msg)

                # record the best performing dna sequence
                if dna_scores[dna] > self.best_score:
                    self.best_score = dna_scores[dna]
                    self.best_mapping = curr_mapping
                    self.best_dna = dna

            # get the current generation average score
            self.avg_scores_per_iter[i] = np.mean(list(dna_scores.values()))
            self.best_scores_per_iter[i] = self.best_score

            # choose the top 5 best performing dna sequence to pass on to the next generation
            sorted_dna_curr_gen = sorted(dna_scores.items(), key=lambda x:x[1], reverse=True)

            self.dna_pool = [sequence[0] for sequence in sorted_dna_curr_gen[:5]]

            if i in np.arange(0,self.NUM_ITER, 50):
                print(
                    f"\n Iter: {i},"
                    f"log likelihood: {self.avg_scores_per_iter[i]}"
                    f"best likelihood so far: {self.best_score},"
                    f"\n decoded_message: \n {self.encoder.decode(encoded_msg, self.best_mapping)}"
                )

# if __name__ == "__main__":
#     GA()._init_dnal_pool()