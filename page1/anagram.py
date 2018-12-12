import random
import sys


def anagram(input_word):
    new_word = list(input_word)
    random.shuffle(new_word)
    return ''.join(new_word)


if __name__ == '__main__':
    result = anagram(sys.argv[1])
    print(result)
