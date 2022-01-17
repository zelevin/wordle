# wordle
Solution for the Riddler of Jan. 14, 2022

The Riddler Classic challenge [https://fivethirtyeight.com/features/when-the-riddler-met-wordle/]
was "to devise a strategy to maximize your probability of winning Wordle in <i>at most three guesses</i>."

Two lists of files were provided: all the words that were the legal Wordle guesses, and all the secret
words that the player had to guess. The first list included the words from the second list.

Naturally, without analyzing the game code, the player does not have access to the second list. This
solution likewise ignores it (naturally, if the space of possible guesses is five times smaller, the
game is considerably less challenging!).

The idea behind the algorithm is straightforward. The first guess is based on zero information, meaning
there is one optimal first move. The third move must be the guess. This means that the second move must be
(1) based entirely on the game's response to the fixed first move, and (2) the game's responses to the
second move must group the possible candidates (i.e., those that returned the given first-word score) into
the <i>largest possible number of groups</i>.

The only additional wrinkle is the handling of the cases when we know the secret word after <i>one</i> guess only.

The files in this repository are:

* wordle_all.txt

The sorted list of all permitted Wordle guesses.

* wordle_precompute_scores.py

To speed up the strategy generation, all the scores are precomputed and saved in a 66Mb file. Run this script first.

* wordle_strategy.py

Analyses possible opening words, returning the probability that the correct word is guessed on the third turn.
If there are N possible candidates after the first two moves, the code considers that the probability of guessing
correctly is 1 / N.

Run this script with the list of opening word candidates as parameters, e.g.:

python wordle_strategy.py slate trace ouija

If there is only one candidate, the script also returns the optimal <i>second</i>-word guesses for each possible
response from the game.

I've ran the above script in batch mode on all permitted words. The best word and score were <b>slate</b> with the
third-guess win probability of <b>0.2533</b>.

* slate.txt

The result of running the script above for the best optimal word <b>slate</b>.

