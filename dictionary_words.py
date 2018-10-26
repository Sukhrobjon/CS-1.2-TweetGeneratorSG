import random
import sys

def read_file():
    words = open("/usr/share/dict/words", "r").read().split('\n')
    return words


def make_random_sentence(num_words):
    new_sentence = []
    words = read_file()
    for _ in range(int(num_words)):
        new_sentence.append(words[random.randint(0, len(words))] + " ")
    return(''.join(new_sentence))

if __name__ == '__main__':
    num_words = sys.argv[1]
    print(make_random_sentence(num_words))
    