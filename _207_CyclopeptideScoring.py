__author__ = 'Reza Moradi'

from _211_Spectrum import import_int_mw_table, generate_spectrum
from collections import Counter


def score(peptide, spectrum, cyclic=True):
    """
    Calculates the score of a cyclic 'peptide' against a 'spectrum'

    :param peptide:
    :type peptide: tuple
    :param spectrum:
    :type spectrum: Counter
    :param cyclic:
    :type cyclic: bool
    :return:
    :rtype: int

    Sample Input:
    NQEL
    0 99 113 114 128 227 257 299 355 356 370 371 484

    Sample Output:
    11
    """

    if len(peptide) == 0:
        return 1

    subtraction = spectrum - Counter(generate_spectrum(peptide, int_mw_table, cyclic))

    return sum(spectrum.values()) - sum(subtraction.values())

int_mw_table = import_int_mw_table('integer_mass_table_2')
# int_mw_table = {str(i): str(i) for i in range(57, 201)}

if __name__ == "__main__":

    peptide_list = input().split(' ')
    spectrum_ = Counter(map(int, input().split(' ')))

    for peptide_ in peptide_list:
        peptide_ = tuple(map(int, peptide_.split('-')))


        print(score(peptide_, spectrum_))
