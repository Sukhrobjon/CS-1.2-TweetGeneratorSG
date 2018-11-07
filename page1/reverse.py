
# version two using slicing notation
def reverse_words(word):
    return word[::-1]
def reverse_sentence(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))
word = 'singleWord'
sentence = "This is a sentence!"
print(reverse_words(word))
print(reverse_sentence(sentence))
