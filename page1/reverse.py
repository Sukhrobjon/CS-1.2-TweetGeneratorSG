# version two using slicing notation
def reverse_words(word):
    '''
        Returns reversed version of the word using slice notation
    '''
    return word[::-1]
def reverse_sentence(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])

if __name__ == '__main__':
    word = 'singleWord'
    sentence = "This is a sentence!"
    print(reverse_words(word))
    print(reverse_sentence(sentence))
