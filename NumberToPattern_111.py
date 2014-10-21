__author__ = 'Reza Moradi'


def number_to_pattern(index, k):

    """ Transforms an integer 'index' into a unique k-mer 'pattern' """

    num_to_nucleotide = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

    # Converting the 'index' into pattern
    pattern = ''
    for i in range(k - 1, -1 , -1):
        # Transforming the 'index', which is a 10-base number, into a 4-base number and then
        # converting each digit of that number to the corresponding letter i.e. 'A', 'T', 'C', 'G'
        pattern += num_to_nucleotide[index // 4 ** i]
        index %= 4 ** i

    return pattern