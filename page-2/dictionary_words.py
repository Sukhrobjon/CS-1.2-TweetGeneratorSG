import random
import sys
import timeit

'''
    opens the file and read from it line by line and return to 
    list of the words 
'''
def read_file():
    with open("/usr/share/dict/words") as file:
        words = file.read().split('\n')
    return words
    
        

'''
    makes a random sentence out of the read_file() with specific number of words
    according tho user input. And returns to sentence splinting the words by single 
    space
'''
def make_random_sentence(num_words):
    new_sentence = []
    words = read_file()
    for _ in range(int(num_words)):
        new_sentence.append(words[random.randint(0, len(words))] + " ")
    return(''.join(new_sentence))

if __name__ == '__main__':
    # number of words user want grab from the file
    
    num_words = sys.argv[1]
    print(make_random_sentence(num_words))
    
    

'''
timeit built in banch mark library
'''