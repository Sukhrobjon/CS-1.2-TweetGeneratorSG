import random
import numpy as np
from words_frequency import * 

# this is on progress for  usage of list or tuple
def cumulative_weight(histogram):
    '''Takes a list and return a cumulative sum of the list'''
    cumulative_list = np.cumsum(histogram)
    return cumulative_list

def weighted_random_choice(histogram_dict):
    '''
        Gets random number according to occurance of the word
    '''
    
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


def sample(histogram_dict):
    '''Keep track of the words and returns a dictionry
    of words and the frequency as key and value pair'''
    result = {}
    
    current_word = (weighted_random_choice(histogram_dict))
    result[current_word] = result.get(current_word, 0) + 1
    return result


if __name__ == '__main__':
    
    source_text = read_file('fish.txt')
    words_list = polishishing_file(source_text)
    histogram = histogram_dict(words_list)
    print("This should work as a dictionary")
    print(histogram)
    print(sample(histogram))

    
