__author__ = 'Reza Moradi'


def number_to_pattern(index, k):

    """
    Transforms an integer 'index' into a unique k-mer 'pattern'

    :param index:
    :type index: int
    :param k:
    :type k: int
    :return:
    :rtype: str
    """

    num_to_nucleotide = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

    # Converting the 'index' into pattern
    pattern = ''
    for i in range(k - 1, -1, -1):
        # Transforming the 'index', which is a 10-base number, into a 4-base number and then
        # converting each digit of that number to the corresponding letter i.e. 'A', 'T', 'C', 'G'
        four_power_i = 4 ** i       # i may get very large, better to be calculated once
        pattern += num_to_nucleotide[index // four_power_i]
        index %= four_power_i

    return pattern