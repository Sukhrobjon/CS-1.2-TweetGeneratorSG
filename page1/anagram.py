import random
import sys


def anagram(input_word):
    '''
        a word, phrase, or name formed by rearranging the letters of another, 
        such as cinema, formed from iceman.
        Returns randomized form of the word(but it doesnt necessarily make sense)
    '''
    new_word = list(input_word)
    random.shuffle(new_word)
    return ''.join(new_word)


if __name__ == '__main__':
    result = anagram(sys.argv[1]) 
    print(result)
