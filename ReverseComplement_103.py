__author__ = 'Reza Moradi'


def reverse_complement(pattern):

    """
    Finds the reverse complement of a DNA string 'pattern'

    :param pattern:
    :type pattern: str
    :return:
    :rtype: str

    Sample Input:
    pattern: AAAACCCGGT

    Sample Output:
    ACCGGGTTTT
    """

    pattern_nucleotides = list(pattern.upper())
    complement_nucleotides = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    # Reverse:
    pattern_nucleotides.reverse()

    # Complement:
    rev_comp_pattern = [complement_nucleotides[nucleotide] for nucleotide in pattern_nucleotides]

    return "".join(rev_comp_pattern)

input_pattern = input("Enter pattern: ").upper()

print(reverse_complement(input_pattern))