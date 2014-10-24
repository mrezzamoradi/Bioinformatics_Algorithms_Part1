__author__ = 'Reza Moradi'
import _108_HammingDistance


def approximate_pattern_matching(pattern, text, d):

    """
    Find all approximate occurrences of a 'pattern' in a string 'text'. An approximate occurrence of the 'pattern'
    is a pattern with at most 'd' mismatches with the 'pattern'

    :param pattern:
    :type pattern: str
    :param text:
    :type text: str
    :param d:
    :type d: int
    :return: All starting positions where 'pattern' appears as a substring of 'text' with at most 'd' mismatches.
    :rtype: list

    Sample Input:
    ATTCTGGA
    CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT
    3

    Sample Output:
    6 7 26 27
    """
    k = len(pattern)
    return [i for i in range(len(text) - k + 1) if _108_HammingDistance.hamming_distance(text[i:i + k], pattern) <= d]