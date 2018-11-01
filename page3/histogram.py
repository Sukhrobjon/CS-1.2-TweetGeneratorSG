import collections
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
    reads the file and return a list of the the words of that file
'''
def read_file():
    with open('source_text.txt') as file:
        source_string = file.read().split(' ')
    return source_string

'''
    counts the frequency of each words using counter library
    and returns dictionry data structure as key: word, value: number
'''
def histogram(source_text):
    count = collections.Counter(source_text)
    return count

def histogram_dict(source_text):
    histogram = {}

    for word in source_text:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram 


'''
    Counts the each word frequency using list of list method
'''
def histogram_list(source_text):
    histogram = []
    current_word = None
    for word in source_text:
        if word == current_word:
            histogram[-1][1] += 1
        else:
            histogram.append([word, 1])
            current_word = word
    return histogram

# returns number of unique words in the source text 
def unique_words(source_text):
    # return len(set(histogram(source_text)))
    # return len(histogram(source_text).keys)
    return len(histogram_dict(source_text))
# print(histogram())

if __name__ == "__main__":
    source_text = read_file()
    # print(histogram(source_text))
    # print(histogram_list(source_text))
    print(unique_words(source_text))
    print(histogram_dict(source_text))
