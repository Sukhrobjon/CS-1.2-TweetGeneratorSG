import random
import numpy as np
# from words_frequency import * I dont know why this line isnt workin
from words_frequency import read_file, getting_words, histogram_dict

# this is on progress for  usage of list or tuple
def cumulative_weight(histogram):
    '''Takes a list and return a cumulative sum of the list'''
    cumulative_list = np.cumsum(histogram)
    return cumulative_list


def weighted_random_choice(histogram_dict):
    '''Gets random number according to weighting of the word occurance'''

    cumulative_num = 0
    sum_values = sum(histogram_dict.values())
    ran_num = random.randint(0, sum_values - 1)

    for key, value in histogram_dict.items():
        cumulative_num += value
        if cumulative_num > ran_num:
            return key
        else:
            continue
    


def sample(histogram_dict, iteration):
    '''Keep track of the words and returns a dictionry
    of words and the frequency as key and value pair'''
    result = {}
    while iteration > 0:
        current_word = (weighted_random_choice(histogram_dict))
        result[current_word] = result.get(current_word, 0) + 1
        iteration = iteration - 1
    return result


if __name__ == '__main__':
    
    source_text = read_file('fish.txt')
    words_list = getting_words(source_text)
    histogram = histogram_dict(words_list)
    print("This should work as a dictionary")
    print(histogram)
    print(sample(histogram, 10000))

    
