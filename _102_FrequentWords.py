__author__ = 'Reza Moradi'


def frequent_words(text, k):

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
    """

    # All possible k-mers with their frequency will be stored in this set:
    kmers = {}

    # Frequency of most frequent k-mer:
    max_frequency = 0

    # Most frequent k-mers will be stored in this list:
    frequent_kmers = []

    for i in range(len(text) - k + 1):
        # Creating a k-mer
        kmer = text[i:i + k]

        # Updating 'kmers' database for 'kmer'
        if kmer not in kmers:
            kmers[kmer] = 1

        else:
            kmers[kmer] += 1

        # Checking if 'kmer' is more frequent than k-mers in 'frequent_kmers'. If so, replace 'kmer' with all
        # those kmers. If 'kmer' is as frequent as those k-mers, add it to the list.
        frequency = kmers[kmer]

        if frequency > max_frequency:
            del frequent_kmers[:]
            max_frequency = frequency
            frequent_kmers.append(kmer)

        elif frequency == max_frequency:
            frequent_kmers.append(kmer)

    frequent_kmers.sort()

    return frequent_kmers

input_text = input("Enter text: ").upper()
input_k = int(input("Enter k: "))

print("\nThe result is:", " ".join(frequent_words(input_text, input_k)))