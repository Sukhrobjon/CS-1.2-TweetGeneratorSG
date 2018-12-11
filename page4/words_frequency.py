import collections
import re
from sample import weighted_random_choice
'''
In this tutorial, we'll be writing a program which, given a source body of text,
can perform operations to answer questions such as:

- What is the least/most frequent word(s)?-not done
- How many different words are used?-not done
- What is the average (mean/median/mode) frequency of words in the text?-not done

The structure to represent this kind of data is called a histogram, which really 
just means a count of things by category. In Python, you can represent a histogram 
in a variety of ways using the different data structures available. Part of the challenge
of this tutorial is how to design and use these data structures to create a histogram.

histogram_list = [['one', 1], ['fish', 4], ['two', 1], ['red', 1], ['blue', 1]]
histogram_tuple = [('one', 1), ('fish', 4), ('two', 1), ('red', 1), ('blue', 1)]
histogram_dictionary = [{'one': 1, 'blue': 1, 'two': 1, 'fish': 4, 'red': 1}]

'''

'''
    reads the file and return a list of the words from the file
'''


def read_file(txt):
    f = open(txt, "r")
    contents = f.read()
    f.close()
    contents = contents.lower()
    contents = strip_pun(contents)
    contents = contents.split()

    return contents


'''returns only words lower case and ignore all other operations'''


def strip_pun(string):
    punc = '''!()-[]{};:"\<>./?@#$%^&*_~1234567890'''
    no_punc = ""
    for char in string:
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
    '''Counts the frequency of each words and returns dictionary'''
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
    count = 0
    if word in histogram:
        count = histogram[word]
    else:
        print("WORD NOT FOUND!!!")
    return count


if __name__ == "__main__":
    source_text = read_file('source_text.txt')
    
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
