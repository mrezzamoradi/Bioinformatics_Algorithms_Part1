__author__ = 'Reza Moradi'

import _111_PatternToNumber


def computing_frequencies(text, k):
    """
    Generates a frequency array for the 'text'. A frequency array of a string 'text' is an array of length 4^k, where
    the i-th element of the array holds the number of times that the i-th k-mer (of a list where all possible k-mers are
    sorted in the lexicographic order) appears in 'text'.

    :param text:
    :type text: str
    :param k:
    :type k: int
    :return:
    :rtype: list

    Sample Input:
    text: AAGCAAAGGTGGG
    k: 2

    list of all possible k-mers: [AA, AC, AG, AT, CA, CC, CG, CT, GA, GC, GG, GT, TA, TC, TG, TT]
    frequency array for 'text':  [3 , 0 , 2 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 3 , 1 , 0 , 0 , 1 , 0 ]

    Sample Output:
    [3 , 0 , 2 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 3 , 1 , 0 , 0 , 1 , 0 ]
    """

    # Initiate frequency array
    frequency_array = [0] * 4 ** k

    nucleotide_to_num = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

    # Calculating frequency of each k-mer in the 'text'
    biggest_order = 4 ** (k-1)

    # For the first k-mer
    kmer = text[:k]
    this_kmer_number = _111_PatternToNumber.pattern_to_number(kmer)
    frequency_array[this_kmer_number] += 1

    # For next k-mers
    for i in range(k, len(text)):
        # Calculating new k-mer number from previous k-mer number
        this_kmer_number = 4 * (this_kmer_number % biggest_order) + nucleotide_to_num[text[i:i + 1]]
        frequency_array[this_kmer_number] += 1

    return frequency_array

if __name__ == "__main__":

    text_ = input()
    k_ = int(input())

    print(computing_frequencies(text_, k_))