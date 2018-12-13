from dictogram  import Dictogram
from cleanup import read_file
from sample import *
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


def cleanup(text):
    """ takes in a text file, opens it and cleans text using regex. outputs
    string of cleaned text """
    with open(text, 'r') as uncleaned_text:
        # print(source_text.read())
        no_chapters = re.sub('[A-Z]{3,}', ' ', uncleaned_text.read())
        remove_periods = re.sub('(\s\.){4,}', '', no_chapters)
        new_text = re.sub('\*', '', remove_periods)
    return new_text


def tokenize(text):
    """ 
    takes in cleaned text as string and makes it into a list of tokens 
    """
    source = text.split()
    return source

def start_word(dictionary):
    start_tokens = []
    for key in dictionary:
        if key[0].islower() is True:
            start_tokens.append(key)
    token = random.choice(start_tokens)
    return token


txt = read_file('source.txt')
# print(markov_chain(txt))
dictionary = Dictogram(txt)
# print(dictionary)
# m_dict = markov_chain(txt)
# print(m_dict)
start_word = (start_word(dictionary))
print(start_word)


sentence = []
sentence.append(start_word)
i = 0
while i < 9:
    new = []
    j = 0
    while j<len(txt) - 1:
        if txt[j] == start_word:
            new.append(txt[j+1])

        j += 1

    m_dict = Dictogram(new)
    start_word = random.choice(list(m_dict.keys()))
    i += 1
    sentence.append(start_word)

print(m_dict)
print(" ".join(sentence) + '.')

