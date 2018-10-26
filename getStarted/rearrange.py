'''
    Shuffles the words without changing the original imput 
'''
import random
import sys

''' 
    returns randomly shuffled list and keeps the original list order
'''
def randomize_list(original_list):
    shuffled_list = original_list[:]
    random.shuffle(shuffled_list)
    return shuffled_list


if __name__ == '__main__':
    original_list = sys.argv[1:]
    print(' '.join(randomize_list(original_list)))

# '_' can be used when you are using this as a iterator and not using 
# it anywhere
'''
    use comments, learn when use while or for loop
    # copies whole list to output_list so when we modify output_list 
    # the input_list doesnt change because of '[:]' symbol
    input_list = []
    output_list = input_list[:]

    # to get rid of the \n line at the end of the file we can use 
    # split(), 

    # open the file one time creating readFunction()


'''
  
