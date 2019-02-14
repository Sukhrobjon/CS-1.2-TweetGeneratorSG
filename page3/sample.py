import random
import numpy as np
import time

# this is on progress for  usage of list or tuple
def cumulative_weight(histogram):
    '''Takes a list and return a cumulative sum of the list'''
    cumulative_list = np.cumsum(histogram)
    return cumulative_list

def weighted_random_choice(histogram_dict):
    '''Returns random word based on frequency of the word'''
    
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
    of words and the frequency'''
    result = {}
    while iteration > 0:
        current_word = (weighted_random_choice(histogram_dict))
        result[current_word] = result.get(current_word, 0) + 1
        # print("key {}: {}".format(count,current_word))
        iteration = iteration - 1
    return result


if __name__ == '__main__':
    start_time = time.time()
    histogram_dict = {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}
    print(sample(histogram_dict, 10000))
    print(f"----{time.time() - start_time} SECONDS-----")
    
