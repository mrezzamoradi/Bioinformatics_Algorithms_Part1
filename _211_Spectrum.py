__author__ = 'Reza Moradi'


def import_int_mw_table(filename):
    """
    Imports amino acids and their masses, and stores them in a dictionary

    :return:
    :rtype: dict
    """
    int_mw_file = open(filename, 'r')

    int_mw_table = {}

    line = int_mw_file.readline()

    while line != '':
        int_mw_table[line[0]] = int(line[2:])

        line = int_mw_file.readline()

    int_mw_file.close()

    return int_mw_table


def generate_spectrum(peptide, int_mw_table, cyclic=False):
    """
    Generates the spectrum of 'peptide'. 'peptide' can be either linear or cyclic. By defual it assumes the 'peptide'
    to be linear ('cyclic'=False)

    :param peptide:
    :type peptide: tuple
    :param int_mw_table:
    :type int_mw_table: dict
    :param cyclic:
    :type cyclic: bool
    :return:
    :rtype: list

    Sample Input:
    NQEL

    Sample Output:
    Linear: 0 113 114 128 129 242 242 257 370 371 484
    Cyclic: 0 113 114 128 129 227 242 242 257 355 356 370 371 484
    """
    if type(peptide) == str:
        peptide = tuple([int_mw_table[amino_acid] for amino_acid in peptide])

    # An ascending list of cumulative masses from the first amino acid to the last amino acid in 'peptide'
    prefix_mass = [0]
    for amino_acid in peptide:
        prefix_mass.append(prefix_mass[-1] + int(amino_acid))

    # Total 'peptide' mass and length
    peptide_mass = prefix_mass[-1]
    peptide_length = len(peptide)

    # Initiate spectrum
    spectrum = [0]

    for i in range(peptide_length):
        for j in range(i + 1, peptide_length + 1):
            sequence_mass = prefix_mass[j] - prefix_mass[i]
            spectrum.append(sequence_mass)

            if cyclic and (i > 0) and (j < peptide_length):
                spectrum.append(peptide_mass - sequence_mass)

    return spectrum

if __name__ == "__main__":

    int_mw_table_ = import_int_mw_table('integer_mass_table_2')
    peptide_ = input()

    result = generate_spectrum(peptide_, int_mw_table_)
    result.sort()
    result = map(str, result)

    print(" ".join(result))