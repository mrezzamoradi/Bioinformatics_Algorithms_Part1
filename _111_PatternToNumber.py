__author__ = 'Reza Moradi'


def pattern_to_number(pattern):

    """
    Transform a k-mer 'pattern' into an integer between 0 and 4^k − 1, where k is length of 'pattern'. a recursive
    solution for this problem, with the same speed, is provided in section "1.12 CS: Converting Patterns to Numbers
    and Vice-Versa" of the textbook, but it does not work with a large 'pattern' since it may exceed maximum allowed
    recursion.

    :param str pattern:
    :type pattern: str
    :return:
    :rtype: int
    """

    # Disassemble the 'pattern'
    pattern_nucleotides = list(pattern.upper())
    nucleotide_to_num = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

    # Calculating the number equal to the 'pattern'
    pattern_nucleotides.reverse()
    number = sum([nucleotide_to_num[pattern_nucleotides[i]] * 4 ** i for i in range(len(pattern_nucleotides))])

    return number