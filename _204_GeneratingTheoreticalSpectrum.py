__author__ = 'Reza Moradi'

from _211_Spectrum import import_int_mw_table, generate_spectrum


if __name__ == "__main__":

    in_peptide = input()
    int_mw_table = import_int_mw_table('integer_mass_table')

    print(" ".join(map(str, generate_spectrum(in_peptide, int_mw_table, cyclic=True))))