with open('/usr/share/dict/words', 'r') as dict_words:
    i = 0
    while i < 5:
        print(dict_words.readline())
        i +=1
