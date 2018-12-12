import collections
import re
'''
histogram_list = [['one', 1], ['fish', 4], ['two', 1], ['red', 1], ['blue', 1]]
histogram_tuple = [('one', 1), ('fish', 4), ('two', 1), ('red', 1), ('blue', 1)]
histogram_dictionary = [{'one': 1, 'blue': 1, 'two': 1, 'fish': 4, 'red': 1}]

'''

'''
    reads the file and return a list of the words from the file
'''
def read_file(txt):
    with open(txt) as file:
        words_list = file.read()
    return words_list



def getting_words(source_text):
    '''returns only words lower case and ignore all other operations'''
    words = re.sub("[^a-zA-Z'\-]", " ", source_text)
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

# returns number of words in the dictionary type histogram, if not found returns 0  
def frequency(word, histogram):
    if word in histogram:
        return histogram[word]
    else:
        return 0
    

def sort_by_key(histogram):
    """Sort the histogram by the keys, alphabetically."""
    if type(histogram) == dict:
        return sorted(histogram.items(), key=lambda x: x[0])
    elif type(histogram) == list:
        return sorted(histogram, key=lambda x: x[0])
    
def sort_hist_val(histogram):
    """Sort the histogram by the values, in ascending order."""
    if type(histogram) == dict:
        return sorted(histogram.items(), key=lambda x: x[1], reverse=True)
    elif type(histogram) == list:
        return sorted(histogram, key=lambda x: x[1], reverse=True)


def write_to_file(histogram):
    """Write the histogram to a file."""
    with open('sorted_source_text.txt', 'w') as file:
        for words in histogram:
            file.write("{0} {1}\n".format(words[0], words[1]))
    return 0

if __name__ == "__main__":
    fish = 'one fish, two. fish! red fish blue fish  '
    # source_text = read_file('source_text.txt')
    source_text = fish
    
    words_list = getting_words(source_text)
    print(histogram_dict(words_list)) # histogram with dictionary

    # print(histogram_list(words_list))
    # print(histogram_tuple(words_list))
    # unique_words = unique_words(histogram_tuple(words_list))
    # print("Number of unique words {}".format(unique_words))
    # print(frequency('fish', histogram_dict(words_list)))
    new_source = read_file('source_text.txt')
    words = getting_words(new_source)
    # print(sort_by_key(histogram_dict(words)))
    print(sort_hist_val(histogram_dict(words[:100])))
    write_to_file(sort_hist_val(histogram_dict(words)))
