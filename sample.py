import random


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
    # return histogram_dict
    return key


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
    print(sample(histogram_dict, 10000))
    print(weighted_random_choice(histogram_dict))

