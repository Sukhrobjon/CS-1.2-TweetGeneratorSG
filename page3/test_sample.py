import random
from histogram import *
import numpy as np

# this is on progress


def cumulative_weight(histogram):
    '''Takes a list and return a cumulative sum of the list'''
    cumulative_list = np.cumsum(histogram)
    return cumulative_list


def weighted_random_choice(histogram_dict):
    '''Gets random number according to weighting of the word'''

    cumulative_num = 0
    sum_values = sum(histogram_dict.values())
    ran_num = random.randint(0, sum_values - 1)

    for key, value in histogram_dict.items():
        cumulative_num += value
        if cumulative_num > ran_num:
            return key
        else:
            continue
    return histogram_dict


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

    histogram_dict = {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}
    print("This should work as a dictionary")
    print(sample(histogram_dict, 100))

    histogram = [['blue', 1], ['fish', 4], ['one', 1], ['red', 1], ['two', 1]]
    # creates a list of tuple containg putting in row and collumns
    words = list(zip(*histogram))

    # print(words)
    my_list = [1, 4, 1, 1, 1]
    # print(cumulative_weight(my_list))
