import numpy as np
from collections import defaultdict

all_words = [word.strip() for word in open('wordle_all.txt')]
score = np.load('wordle.npz')['scores']

first_move = True
words = list(range(len(all_words)))
while len(words) > 1:
    if first_move:
        first_move = False
        guess = all_words.index('slate')
    elif len(words) == 1:
        guess = words[0]
    else:
        best_groups = 0
        for g in range(len(all_words)):
            groups = defaultdict(list)
            for w in words:
                groups[score[w, g]] += [w]
            if len(groups) == len(words):
                guess = g
                break
            if len(groups) > best_groups:
                best_groups, guess = len(groups), g
    ask = True
    while ask:
        s = input(all_words[guess] + '? ').lower()
        if len(s) == 5 and sum(s.count(c) for c in '_yg') == 5:
            ask = False
        else:
            print('This response doesn\'t scan.')
    s = sum(3 ** i * '_yg'.index(c) for i, c in enumerate(s))
    words = [w for w in words if score[w, guess] == s]

print(all_words[words[0]] if len(words) == 1 else 'I give up!')