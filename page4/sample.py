import random
import words_frequency

def weighted_choice(histogram):
    
    word = random.choice(histogram)
    return word


# homework write down the answers for the questions on page 6
if __name__ == '__main__':
    histogram = [['blue', 1], ['fish', 4], ['one', 1], ['red', 1], ['two', 1]]
    words = list(zip(*histogram))
    # print(list(words[1]))
    
    iteration = 10
    result = {}
    while iteration > 0:
        current_word = weighted_choice(words[0])
        result[current_word] = result.get(current_word, 0) + 1
        iteration = iteration - 1
    print(result)