__author__ = 'Reza Moradi'

from _211_Spectrum import import_int_mw_table


def peptide_counter(total_mass):
    global peptide_list

    if total_mass == 0:
        found.add(total_mass)
        peptide_list += 1

    for aa in amino_acid_list_:
        if total_mass >= int_mw_table_[aa]:
            peptide_counter(total_mass - int_mw_table_[aa])


int_mw_table_ = import_int_mw_table('integer_mass_table_2')
amino_acid_list_ = 'GASPVTCINDKEMHFRYW'
found = set()
peptide_list = 0

peptide_counter(520)

print(peptide_list)
