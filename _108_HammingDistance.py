__author__ = 'Reza Moradi'


def hamming_distance(text1, text2):

    """
    The number of mismatches between texts 'text1' and 'text2' is called the Hamming distance between these texts

    :param text1:
    :type text1: str
    :param text2:
    :type text2: str
    :return:
    :rtype: int

    Sample Input:
    GGGCCGTTGGT
    GGACCGTTGAC

    Sample Output:
    3
    """

    return sum([1 for i in range(len(text1)) if text1[i] != text2[i]])