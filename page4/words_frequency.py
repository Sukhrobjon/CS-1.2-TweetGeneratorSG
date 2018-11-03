import collections
import re
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


def read_file():
    with open('source_text.txt') as file:
        words_list = file.read()
    return words_list


'''returns only words lower case and ignore all other operations'''


def polishishing_file(source_text):
    words = re.sub("[^a-zA-Z'\\-]", " ", source_text)
    return words.lower().split()


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
    source_text = read_file()
    words_list = polishishing_file(source_text)
    print(histogram_dict(words_list))
    print(histogram_list(words_list))
    print(histogram_tuple(words_list))
    unique_words = unique_words(histogram_tuple(words_list))
    print("Number of unique words {}".format(unique_words))
    print(frequency('the', histogram_dict(words_list)))
