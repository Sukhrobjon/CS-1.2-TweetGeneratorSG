
# version one using loop it is still on progress not working properly yet
def reverse_words_one(word):
    start = 0
    end = len(word)-1
    while start < end:
        word[start], word[end] = word[end], word[start]
        start += 1
        end -= 1
    return word

# version two using slicing notation
def reverse_words_two(word):
    return word[::-1]

word = 'Sukhrob'

print(reverse_words_two(word))
