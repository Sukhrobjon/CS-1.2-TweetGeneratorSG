from collections import Counter
import re
'''
histogram_list = [['one', 1], ['fish', 4], ['two', 1], ['red', 1], ['blue', 1]]
histogram_tuple = [('one', 1), ('fish', 4), ('two', 1), ('red', 1), ('blue', 1)]
histogram_dictionary = [{'one': 1, 'blue': 1, 'two': 1, 'fish': 4, 'red': 1}]

'''


def read_file(txt):
    """Reads the file and return a list of the words from the file"""
    with open(txt) as file:
        words_list = file.read()
    return words_list


def getting_words(source_text):
    """Returns lower cased words and ignore all other operations"""
    words = re.sub("[^a-zA-Z'\-]", " ", source_text)
    return words.lower().split()


def histogram(source_text):
    """ Counts the frequency of each words using counter class from collection library
        and returns dictionry data structure as key: word, value: number
    """
    count = Counter(source_text)
    return count


def histogram_dict(source_text):
    """Counts the frequency of each words and returns dictionary"""
    histogram = {}

    for word in source_text:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram


def histogram_list(source_text):
    """Counts the each word frequency and returns list of list."""
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
    """Counts the each word frequency and returns list of list."""
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


def unique_words(histogram):
    """Returns number of unique words in the source text"""
    return len(histogram)


def frequency(word, histogram):
    """Returns number of words in the dictionary type histogram, if not found returns 0"""
    if word in histogram:
        return histogram[word]
    else:
        return 0



if __name__ == "__main__":
    source_text = read_file('fish.txt')

    words_list = getting_words(source_text)
    print("Histogram Dictionary: ", histogram_dict(words_list))  # histogram_dictionary
    print("List of lists: ", histogram_list(words_list))
    print("List of tuples: ", histogram_tuple(words_list))
    unique_words = unique_words(histogram_tuple(words_list))
    print("Number of unique words {}".format(unique_words))
    frequency_of_word = frequency('one', histogram_dict(words_list))
    print("The {} is occured {} time(s).".format('one', frequency_of_word))
    
    

    

    
    
    
    
    i = 0
    # sentence = []
    # while i < 10:
    #     sentence.append(weighted_random_choice(histogram))
    #     i += 1

    # print(sentence)
    
