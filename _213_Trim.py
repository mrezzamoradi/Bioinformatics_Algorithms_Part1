__author__ = 'Reza Moradi'

from _207_CyclopeptideScoring import score
from collections import Counter


def trim(leaderboard, spectrum, n):
    """
    Returns the 'n' highest-scoring linear peptides on 'leaderboard' with respect to 'spectrum'.

    :param leaderboard:
    :type leaderboard: set
    :param spectrum:
    :type spectrum: Counter
    :param n:
    :type n: int
    :return:
    :rtype: set

    Sample Input:
    LAST ALST TLLT TQAS
    0 71 87 101 113 158 184 188 259 271 372
    2

    Sample Output:
    LAST ALST
    """
    if len(leaderboard) == 0:
        return leaderboard

    # Peptides and their scores would be stored in:
    scoreboard = Counter()
    new_leaderboard = set()

    # Building 'scoreboard'
    for peptide in leaderboard:
        scoreboard[peptide] = score(peptide, spectrum, cyclic=False)

    # 'n' must be smaller than scoreboard (leaderboard) size
    if n > len(scoreboard):
        n = len(scoreboard)

    # n top-score peptides
    top_scorers = scoreboard.most_common(n)

    # Adding the top-score peptides to a new leaderboard
    for peptide_and_score in top_scorers:
        new_leaderboard.add(peptide_and_score[0])

    # Including ties
    last_ones_score = top_scorers[-1][1]
    for peptide, sc in scoreboard.items():
        if sc == last_ones_score:
            new_leaderboard.add(peptide)

    return new_leaderboard