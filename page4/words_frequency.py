import collections
import re
from sample import weighted_random_choice

'''
    histogram_list = [['one', 1], ['fish', 4], ['two', 1], ['red', 1], ['blue', 1]]
    histogram_tuple = [('one', 1), ('fish', 4), ('two', 1), ('red', 1), ('blue', 1)]
    histogram_dictionary = [{'one': 1, 'blue': 1, 'two': 1, 'fish': 4, 'red': 1}]
'''




def read_file(txt):
    """Reads the file and return a list of the words from the file"""
    
    f = open(txt, "r")
    contents = f.read()
    f.close()
    contents = contents.lower()
    contents = strip_pun(contents)
    contents = contents.split()

    return contents


'''returns only words lower case and ignore all other operations'''


def strip_pun(txt):
    # punc = '''!()-[]{};:"\<>./?@#$%^&*_~1234567890'''
    punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    no_punc = ""
    for char in txt:
        if char not in punc:
            no_punc += char

    return no_punc


'''
    counts the frequency of each words using counter library
    and returns dictionry data structure as key: word, value: number
'''


def histogram(source_text):
    count = collections.Counter(source_text)
    return count


def histogram_dict(source_text):
    '''
        Counts the frequency of each words and returns dictionary
    '''
    histogram = {}

    for word in source_text:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram


def histogram_list(source_text):
    '''Counts the each word frequency and returns list of list '''
    source_text.sort()
    histogram = []
    current_word = None
    for word in source_text:
        if word == current_word:
            histogram[-1][1] += 1
        else:
            histogram.append([word, 1])
            current_word = word
    return histogram


def histogram_tuple(source_text):
    '''Counts the each word frequency and returns list of list '''
    source_text.sort()
    histogram = []
    current_word = None
    for word in source_text:
        if word == current_word:
            histogram[-1] = (word, histogram[-1][1]+1)
        else:
            histogram.append((word, 1))
            current_word = word
    return histogram

# returns number of unique words in the source text


def unique_words(histogram):
    return len(histogram)

# returns number of words in the histogram


def frequency(word, histogram):
    if word in histogram:
        return histogram[word]
    else:
        print("WORD NOT FOUND!!!")
    return 0


if __name__ == "__main__":
    source_text = read_file('fish.txt')
    
    histogram = histogram_dict(source_text)
    print(histogram_dict(source_text))
    i = 0
    sentence = []
    while i < 10:
        sentence.append(weighted_random_choice(histogram))
        i += 1

    print(sentence)
    





    # print(histogram_list(words_list))
    # print(histogram_tuple(words_list))
    # unique_words = unique_words(histogram_tuple(words_list))
    # print("Number of unique words {}".format(unique_words))
    # print(frequency('the', histogram_dict(words_list)))
