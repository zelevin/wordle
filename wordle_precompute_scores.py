import numpy as np

def score(secret, guess):
    s, g, out = list(secret), list(guess), 0
    for i in range(5):
        if s[i] == g[i]:
            out += 3 ** i * 2
            s[i] = g[i] = ''
    for i in range(5):
        if g[i] and g[i] in s:
            out += 3 ** i
            s[s.index(g[i])] = g[i] = ''
    return out

all_words = [word.strip() for word in open('wordle_all.txt')]
size = len(all_words)
scores = np.empty((size, size), dtype = np.ubyte)
for s, secret in enumerate(all_words):
    print('{:.1%}'.format(s / size), end = '\r')
    for g, guess in enumerate(all_words):
        scores[s, g] = score(secret, guess)
    
np.savez_compressed('wordle', scores = scores)