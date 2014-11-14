__author__ = 'Reza Moradi'

from _211_Spectrum import import_int_mw_table
from _207_CyclopeptideScoring import score
from _206_CyclopeptideSequencing import expand_list
from _213_Trim import trim
from collections import Counter


def lb_cyclopeptide_sequencing(spectrum, int_mw_table, n):
    """
    Finds all cyclic peptide having maximum score against an experimental 'spectrum'

    :param spectrum:
    :type spectrum: Counter
    :param n:
    :type n: int
    :return:
    :rtype: list

    Sample Input:
    10
    0 71 113 129 147 200 218 260 313 331 347 389 460

    Sample Output:
    113-147-71-129
    """

    # Peptides with eligible scores will be stored in:
    leaderboard = {"Just to enter while loop below"}

    # Leader-peptide score (max score of current peptides)
    leader_peptide_score = 0

    # Leader peptides will be stored in:
    leader_peptides = set()

    # Mass of the peptide willing to find (target peptide)
    parent_mass = max(spectrum)

    # Do this while we have eligible peptides
    while len(leaderboard) != 0:
        # We have entered the loop now :D
        if leaderboard == {"Just to enter while loop below"}:
            leaderboard.clear()

        # Expand eligible peptides
        leaderboard = expand_list(leaderboard, int_mw_table)
        leaderboard_copy = leaderboard.copy()

        for peptide in leaderboard_copy:
            # Total mass of this 'peptide'
            peptide_mass = sum(map(int, peptide))

            # If 'peptide' has the same mass as 'target peptide', check it to make sure it has a same spectrum as
            # 'target peptide' has (the 'spectrum')
            if peptide_mass == parent_mass:
                peptide_score = score(peptide, spectrum, cyclic=True)

                # Find the best among the bests :D
                if peptide_score > leader_peptide_score:
                    leader_peptide_score = peptide_score
                    leader_peptides.clear()

                if peptide_score == leader_peptide_score:
                    leader_peptides.add(peptide)

            # If 'peptide' has a bigger mass than the 'target peptide', remove it from eligible peptides list
            elif peptide_mass > parent_mass:
                leaderboard.remove(peptide)

        # To avoid accumulation of peptides, select the first 'n' top-score peptides and cut the rest
        if len(leaderboard) != 0:
            leaderboard = trim(leaderboard, spectrum, n)

    return ["-".join(peptide) for peptide in leader_peptides]


if __name__ == "__main__":

    N = int(input())
    spectrum_ = Counter(map(int, input().split(' ')))

    print(" ".join(lb_cyclopeptide_sequencing(spectrum_, import_int_mw_table('integer_mass_table_2'), N)))