__author__ = 'Reza Moradi'

import _111_ComputingFrequencies
import _111_NumberToPattern


def faster_frequent_words(text, k):

    """
    This function finds the most frequent k-mers in a text

    :param str text:
    :param int k:
    :return:
    :rtype: list

    Sample Input:
    text: ACGTTGCATGTCGCATGATGCATGAGAGCT
    k: 4

    Sample Output:
    CATG GCAT

    P.S. In practice, this function was not faster than 'frequent_words' function in '_102_FrequentWords.py' as
    the name of the function suggests. I uploaded it because it uses a different method to solve the problem of
    finding frequent words and I think it has a potential to get optimized and faster than the 'frequent_words'
    function.
    - Reza Moradi
    """

    frequency_array = _111_ComputingFrequencies.computing_frequencies(text, k)

    # Frequency of most frequent k-mer
    max_frequency = max(frequency_array)

    # Search in 'frequency_array' and find indices of most frequent k-mers
    frequent_kmers_indices = [i for i, frequency in enumerate(frequency_array) if frequency == max_frequency]

    # Converting indices into corresponding k-mers
    frequent_kmers = [_111_NumberToPattern.number_to_pattern(index, k) for index in frequent_kmers_indices]

    return frequent_kmers

if __name__ == "__main__":

    input_text = input("Enter text: ").upper()
    input_k = int(input("Enter k: "))

    print("\nThe result is:", " ".join(faster_frequent_words(input_text, input_k)))