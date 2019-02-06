from dictogram  import Dictogram
from cleanup import read_file
from sample import weighted_random_choice
import re
import random


def markov_chain(txt):
    m_chain = {}
    for word in txt[:-1]:
        if word not in m_chain:
            i = 0
            fol_word = []
            while i < len(txt) - 1:
                if txt[i] == word:
                    fol_word.append(txt[i+1])
                i += 1
            m_chain[word] = Dictogram(fol_word)
    return m_chain

def start(dictionary):
    """
        Return a start token according to word's weight at the start of sentence
    """
    # creating a dict with only Capitilized words
    start_tokens = {k: v for (k, v) in dictionary.items() if k.islower() is False}
    token = weighted_random_choice(start_tokens)
    # print("start tokens ", start_tokens)
    return token


def make_sentence_with_markov(sent_len):
    txt = read_file('source.txt')

    dictionary = Dictogram(txt)
    start_word = (start(dictionary))
    
    sentence = []
    sentence.append(start_word)
    i = 0
    while i < sent_len:
        new = []
        j = 0
        while j<len(txt) - 1:
            if txt[j] == start_word:
                new.append(txt[j+1])

            j += 1

        m_dict = Dictogram(new)
        # next_word = random.choice(list(m_dict.keys()))
        next_word = weighted_random_choice(m_dict)
        start_word = next_word
        i += 1
        sentence.append(start_word)

    # print(m_dict)
    return (" ".join(sentence) + '.')


print(make_sentence_with_markov(25))