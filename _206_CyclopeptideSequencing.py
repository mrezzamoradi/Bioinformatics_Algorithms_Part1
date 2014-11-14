__author__ = 'Reza Moradi'

from _211_Spectrum import import_int_mw_table, generate_spectrum


def expand_list(peptide_list, int_mw_table):
    """
    Expands all peptides of 'peptide_list', by adding amino acids at the end of each peptide

    :param peptide_list:
    :type peptide_list: set
    :param int_mw_table:
    :type int_mw_table: dict
    :return:
    :rtype: set
    """

    # Expanded peptides will be stored in:
    expanded_list = set()

    if len(peptide_list) == 0:
        # For the first expansion (initiate 'peptide_list'):
        for amino_acid in int_mw_table.values():
            expanded_list.add((str(amino_acid),))
    else:
        for peptide in peptide_list:
            for amino_acid in int_mw_table.values():
                new_peptide = peptide + (str(amino_acid),)
                expanded_list.add(new_peptide)

    return expanded_list


def cyclopeptide_sequencing(spectrum):
    """
    Finds peptides with theoretical spectrum equal to 'spectrum' using Branch-and-Bound algorithm.

    :param spectrum:
    :type spectrum: set
    :return:
    :rtype: list

    Sample Input:
    0 113 128 186 241 299 314 427

    Sample Output:
    186-128-113 186-113-128 128-186-113 128-113-186 113-186-128 113-128-186
    """

    int_mw_table = import_int_mw_table('integer_mass_table_2')

    # List of peptides with consistent spectra
    possible_list = {'Just to enter while loop below'}

    while len(possible_list) != 0:
        if possible_list == {'Just to enter while loop below'}:
            possible_list = set()

        # A copy of eligible peptides, before being expanded
        final_list = possible_list.copy()

        # Expand the eligible peptides
        possible_list = expand_list(possible_list, int_mw_table)

        # A copy of 'possible_list' to use in for loop
        possible_list_copy = possible_list.copy()

        for peptide in possible_list_copy:
            # This algorithm generates ALL possible linear forms of a cyclopeptide, so it's not necessary to calculate
            # cyclospectrum of each eligible peptide. Also, a linear spectrum of a peptide is always consistent with its
            # cyclospectrum (linear spectrum is a subset of cyclospectrum).
            if not set(generate_spectrum(peptide, int_mw_table)).issubset(spectrum):
                possible_list.remove(peptide)

        if len(possible_list) == 0:
            return ["-".join(peptide) for peptide in final_list]

if __name__ == "__main__":

    spectrum_string = input()
    spectrum_list = spectrum_string.split(' ')
    spectrum_ = set(map(int, spectrum_list))

    print(" ".join(cyclopeptide_sequencing(spectrum_)))