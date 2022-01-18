# wordle
Solution for the Riddler of Jan. 14, 2022

The [Riddler Classic challenge](https://fivethirtyeight.com/features/when-the-riddler-met-wordle/)
was "to devise a strategy to maximize your probability of winning Wordle in *at most three guesses*."

Two lists of files were provided: all the words that were the legal Wordle guesses, and all the
possible secret words. The first list included the words from the second list.

Naturally, without analyzing the game code, the player does not have access to the second list. This
solution likewise ignores it (naturally, if the space of possible guesses is five times smaller, the
game is considerably less challenging!).

The idea behind the algorithm is straightforward. The first guess is based on zero information, meaning
there is one optimal first move. The third move must be the guess. This means that the second move must be
(1) based entirely on the game's response to the fixed first move, and (2) the game's responses to the
second move must group the possible candidates (i.e., those that returned the given first-word score) into
the *largest possible number of groups*.

The only additional wrinkle is the handling of the cases when we know the secret word after *one* guess only.

The files in this repository are:

[wordle_all.txt](wordle_all.txt)

The sorted list of all permitted Wordle guesses.

[wordle_precompute_scores.py](wordle_precompute_scores.py)

To speed up the strategy generation, all the scores are precomputed and saved in a compressed numpy file.
Run this script first. It takes ~3 minutes and creates a ~66Mb file.

[wordle_strategy.py](wordle_strategy.py)

Analyses possible opening words, returning the probability that the correct word is guessed on the third turn
for the given combination of the first word response and the (optimal for this response) second guess. Also
computes the total weighted probability for the opening move. If there are N possible candidates after the
first two moves, the code considers that the probability of guessing correctly is 1 / N.

Run this script with the list of opening word candidates as parameters, e.g.:
```
python wordle_strategy.py slate trace ouija
```
If there is only one candidate, the script returns the extended analysis, including the optimal *second*-word
guesses for each possible *first*-word response from the game. In those cases where the third guess is required
but would determine the secret word uniquely, each possible *second*-word response is provided along with the
unque secret word for the third guess.

For example, in the file below (for the opening word **slate**), one line reads:
```
GYG_G cahow 1.0000 YY___: scale, _YY__: shale, _Y___: spale, _Y__Y: swale
```
This means that if the first-word response was "green, yellow, green, blank, green", the second move should be
"cahow", which will result in the secret being guessed on the third turn with the probability of 1.0.  If the
response to this second word is "yellow, yellow, blank, blank, blank", then the secret word is "scale"; if the
second-word response is "blank, yellow, yellow, blank, blank", then the secret word is "shale", etc.

I've ran the above script in batch mode on all permitted words. The best word and score were **slate** with the
third-guess win probability of **0.2533**.

[wordle_slate.txt](wordle_slate.txt)

The result of running the script above for the best optimal word <b>slate</b>.

I've also run a slightly modified version of the above script that is aware of the secret words list. In this case,
the optimal first move is **trace**, with the third-move winning probability of **0.5996**.

[wordle_play.py](wordle_play.py)

The script that actually uses the above algorithm dynamically to play without any knowledge of secret words. The
responses should be entered in the same format as above (e.g., "__g_y"), case-insensitively.

Note that this script will keep refining until it is certain, as opposed to the problem above, where the aim is
to refine as much as possible in the first two moves and then take a guess, if needed, on the third attempt.
