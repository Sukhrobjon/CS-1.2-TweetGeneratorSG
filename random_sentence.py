import random
from sample import weighted_random_choice

'''
    opens the file and read from it line by line and return to 
    list of the words 
'''


def read_file(source):
    with open(source) as file:
        words = file.read().split()
    return words


def make_random_sentence(num_words):
    '''makes a random sentence out of the read_file() with specific number of words
    according tho user input. And returns to sentence splinting the words by single 
    space'''
    source = 'source.txt'
    new_sentence = []
    his = weighted_random_choice()
    words = read_file(source)
    for _ in range(int(num_words)):
        new_sentence.append(words[random.randint(0, len(words))] + " ")
    return(''.join(new_sentence))


if __name__ == '__main__':

    # num_words = sys.argv[1]
    num_words = 10
    print(make_random_sentence(num_words))


'''
timeit built in banch mark library
'''
