from dictogram  import Dictogram

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

x = 'one fish two fish blue fish red fish one fish'
txt = x.split()
print(markov(txt))
