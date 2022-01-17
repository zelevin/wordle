import numpy as np
from sys import argv
from collections import defaultdict

all_words = [word.strip() for word in open('wordle_all.txt')]
all_scores = np.load('wordle.npz')['scores']

def analyze(first):
    groups = defaultdict(list)
    for secret in range(len(all_words)):
        groups[all_scores[secret, first]] += [secret]        
    strategy = {first_score: (1.0, secrets[0]) if len(secrets) == 1 else
        max((len(set(all_scores[secret, j] for secret in secrets)) / len(secrets), j) for j in range(len(all_words)))
        for first_score, secrets in groups.items()}
    return strategy, sum(strategy[first_score][0] * len(secrets) for first_score, secrets in groups.items()) / len(all_words)

def score_to_str(s):
    return ''.join('_YG'[s // 3 ** i % 3] for i in range(5))

for first in argv[1:]:
    if first in all_words:
        strategy, prob = analyze(all_words.index(first))
        print('{} = {:.4f}'.format(first, prob))
        if len(argv) == 2:
            for k, (prob, second) in sorted(strategy.items()):
                print('{} {} {:.4f}'.format(score_to_str(k), all_words[second], prob))
    else:
        print('\'{}\' is not a permitted word'.format(first))