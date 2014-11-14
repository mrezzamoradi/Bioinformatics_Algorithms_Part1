__author__ = 'Reza Moradi'

from _202_ProteinTranslation import ribosome, import_codon_table
from _103_ReverseComplement import reverse_complement


def transcribe(dna):
    """
    Transcribes a DNA sequence 'dna' into RNA

    :param dna:
    :type dna: str
    :return:
    :rtype: str
    """

    rna = ''

    for nucleotide in dna:
        if nucleotide == 'T':
            rna += 'U'
        else:
            rna += nucleotide

    return rna


def peptide_encoding(dna, peptide):
    """
    a DNA subsequence 'pattern' encodes an amino acid string 'peptide' if the RNA string transcribed from either
    'pattern' or its reverse complement translates into 'peptide'

    :param dna:
    :type dna: str
    :param peptide:
    :type peptide: str
    :return:
    :rtype: list

    Sample Input:
    ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
    MA

    Sample Output:
    ATGGCC
    GGCCAT
    ATGGCC
    """

    codon_table = import_codon_table()

    # Length of the 'pattern' must be 3 times the length of the 'peptide', since each aminoacid is
    pattern_length = 3 * len(peptide)
    encoding_patterns = []

    # 'pattern' and its reverse-complement
    pattern = dna[:pattern_length]
    rev_pattern = reverse_complement(pattern)

    for nucleotide in dna[pattern_length:]:

        # Translating 'pattern' and its reverse-complement
        pattern_translation = ribosome(transcribe(pattern), codon_table)
        rev_pattern_translation = ribosome(transcribe(rev_pattern), codon_table)

        # Checking if the translations are equal to the 'peptide'
        if (pattern_translation == peptide) or (rev_pattern_translation == peptide):
            encoding_patterns.append(pattern)

        pattern = pattern[1:] + nucleotide
        rev_pattern = reverse_complement(nucleotide) + rev_pattern[:-1]

    return encoding_patterns

if __name__ == "__main__":
    dna_string = input()
    peptide_string = input()

    print("\n".join(peptide_encoding(dna_string, peptide_string)))