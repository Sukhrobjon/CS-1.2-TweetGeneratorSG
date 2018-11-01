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


def histogram():
    source_text = open('source_text.txt').read().split(' ')
    count = collections.Counter(source_text)
    return count


print(histogram())

