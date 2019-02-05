import random
import sys


def randomize_list(original_list):
    ''' 
        Returns randomly shuffled list of words and keeps the original list order
    '''
    shuffled_list = original_list[:]
    random.shuffle(shuffled_list)
    return shuffled_list


if __name__ == '__main__':
    original_list = sys.argv[1:]
    print('Original List: ', original_list)
    print('Shuffled List:',' '.join(randomize_list(original_list)))








'''
    **Side notes: for the class 2 and code review for rearrange the words**
    1. use comments, learn when use while or for loop
    # copies whole list to output_list so when we modify output_list 
    # the input_list doesnt change because of '[:]' symbol(means copying from 0th 
    # to the last element of the list)
    
    input_list = []
    output_list = input_list[:]

    to get rid of the '\n' line at the end of the file we can use split(), 

    - open the file one time creating readFunction()

    - '_' can be used when you are iteratating smth with for loop and you dont have
      to use specific variable for that

'''
  
