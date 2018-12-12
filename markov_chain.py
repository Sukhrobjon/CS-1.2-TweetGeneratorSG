from dictogram  import Dictogram
from cleanup import read_file, polishing_text 
def markov(txt):
    m_chain = {}
    for word in txt[:-1]:
        if word not in m_chain:
            i = 0
            fol_word = []
            while i < len(txt) - 1:
                if txt[i] == word:
                    fol_word.append(txt[i+1])
                i += 1
            m_chain[word] = Dictogram(fol_word)
    return m_chain


txt = read_file('fish_example.txt')
print(markov(txt))
