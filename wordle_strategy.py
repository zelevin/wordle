import numpy as np
from sys import argv
from collections import defaultdict

all_words = [word.strip() for word in open('wordle_all.txt')]
all_scores = np.load('wordle.npz')['scores']

def score_to_str(s):
    return ''.join('_YG'[s // 3 ** i % 3] for i in range(5))

def analyze(first):
    groups = defaultdict(list)
    for secret in range(len(all_words)):
        groups[all_scores[secret, first]] += [secret]        
    strategy, total_count = {}, 0
    for first_score, secrets in groups.items(): 
        third = ''
        if len(secrets) == 1:
            count, second = 1.0, secrets[0]
        else:
            best_groups = {}
            for j in range(len(all_words)):
                candidates = defaultdict(list)
                for secret in secrets:
                    candidates[all_scores[secret, j]] += [secret]
                if len(candidates) > len(best_groups):
                    best_groups, best_second = candidates, j
                if len(candidates) == len(secrets):
                    break
            count, second = len(best_groups), best_second
            if count == len(secrets):
                third = ', '.join(score_to_str(k) + ': ' + all_words[v[0]] for k, v in best_groups.items())
        strategy[first_score] = count / len(secrets), second, third
        total_count += count
    return strategy, total_count / len(all_words)

for first in argv[1:]:
    if first in all_words:
        strategy, prob = analyze(all_words.index(first))
        print('{} = {:.4f}'.format(first, prob))
        if len(argv) == 2:
            for k, (prob, second, third) in sorted(strategy.items()):
                print('{} {} {:.4f} {}'.format(score_to_str(k), all_words[second], prob, third))
    else:
        print('\'{}\' is not a permitted word'.format(first))