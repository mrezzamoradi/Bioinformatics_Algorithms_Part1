__author__ = 'Reza Moradi'


def import_codon_table():
    """
    Imporsts codon and its corresponding aminoacid and stores them in a dictionary
    :return:
    :rtype: dict
    """

    codonfile = open('codon_table', 'r')

    codon_table = {}

    line = codonfile.readline()

    while line != '':
        codon_table[line[:3]] = line[4]
        if codon_table[line[:3]] == '\n':
            codon_table[line[:3]] = '*'

        line = codonfile.readline()

    codonfile.close()

    return codon_table


def ribosome(m_rna, codon_table):
    """
    Simulates the function of a ribosome. Translates messenger RNA 'm_rna' into a polypeptide

    :param m_rna:
    :type m_rna: str
    :return:
    :rtype: str

    Sample Input:
    AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

    Sample Output:
    MAMAPRTEINSTRING
    """

    rna_length = len(m_rna)
    aminoacid = ''
    polypeptide = ''

    i = 0
    while (aminoacid != '*') and (i < rna_length):
        codon = m_rna[i:i+3]
        aminoacid = codon_table[codon]

        if aminoacid != '*':
            polypeptide += aminoacid

        i += 3

    return polypeptide

if __name__ == "__main__":

    in_codon_table = import_codon_table()
    rna_string = input().upper()

    print(ribosome(rna_string, in_codon_table))