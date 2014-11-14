__author__ = 'Reza Moradi'

from _207_LeaderboardCyclopeptideSequencing import lb_cyclopeptide_sequencing
from _209_SpectralConvolution import spectral_convolution
from collections import Counter


def convolution_cycpeptide_sequencing(spectrum, n, m):

    def is_amino_acid(mass):
        return 57 <= mass <= 200

    # Find amino acids among spectral convolution
    amino_acids = filter(is_amino_acid, spectral_convolution(spectrum))
    amino_acids = Counter(amino_acids)

    # Amino acids which can be in the peptide we willing to find (target peptide)
    possible_aa = [amino_acid for amino_acid, multiplicity in amino_acids.most_common(m)]

    # Including ties
    last_ones_mult = amino_acids.most_common(m)[-1][1]
    for aa, mult in amino_acids.items():
        if mult == last_ones_mult:
            possible_aa.append(aa)

    possible_aa = {str(aa): aa for aa in possible_aa}

    return lb_cyclopeptide_sequencing(Counter(map(int, spectrum)), possible_aa, n)

if __name__ == "__main__":

    M = int(input())
    N = int(input())
    spectrum_ = input().split(' ')

    print(" ".join(convolution_cycpeptide_sequencing(spectrum_, N, M)))