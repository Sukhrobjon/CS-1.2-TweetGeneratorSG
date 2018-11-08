import random
import words_frequency
import numpy as np

def cumulative_weight(histogram_dict):
    cumulative_list = np.cumsum(histogram)
    return cumulative_list

def weighted_choice(histogram_dict):
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

# homework write down the answers for the questions on page 6
if __name__ == '__main__':
    histogram = [['blue', 1], ['fish', 4], ['one', 1], ['red', 1], ['two', 1]]
    histogram_dict = {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}
    # creates a list of tuple containg putting in row and collumns 
    words = list(zip(*histogram))  
    
    # print(words)
    my_list = [1, 4, 1, 1, 1]
    # print(cumulative_weight(my_list))
    iteration = 10000
    result = {}
    while iteration > 0:
        current_word = (weighted_choice(histogram_dict))
        result[current_word] = result.get(current_word, 0) + 1
        iteration = iteration - 1
    print(result)
