__author__ = 'Reza Moradi'
# Comment: I don't know what I've done here when I wrote it last year. I have no time to dig it. It just works.
# - Reza Moradi


def mutation_generator(n, m, p, cn, cm, cp, pattern, mutated_kmers_list, d):

    """
    Generates all possible mutations of the 'pattern' (excluding the pattern itself)

    :param n:
    :param m:
    :param p:
    :param cn:
    :param cm:
    :param cp:
    :param pattern:
    :param mutated_kmers_list:
    :param d:
    :return:
    :rtype: None
    """
    valid_chars = ['A', 'T', 'C', 'G']
    if n is None:
        if d >= 1:
            for i in range(len(pattern)):
                for nucleotide in valid_chars:
                    if nucleotide == pattern[i]:
                        continue
                    new_pattern = pattern[:i] + nucleotide + pattern[i + 1:]
                    mutation_generator(i, m, p, nucleotide, cm, cp, new_pattern, mutated_kmers_list, d)

    elif m is None:
        if d >= 2:
            for i in range(n + 1, len(pattern)):
                for nucleotide in valid_chars:
                    if nucleotide == pattern[i]:
                        continue
                    new_pattern = pattern[:i] + nucleotide + pattern[i + 1:]
                    mutation_generator(n, i, p, cn, nucleotide, cp, new_pattern, mutated_kmers_list, d)
        mutated_kmers_list.append(pattern)

    elif p is None:
        if d >= 3:
            for i in range(m + 1, len(pattern)):
                for nucleotide in valid_chars:
                    if nucleotide == pattern[i]:
                        continue
                    new_pattern = pattern[:i] + nucleotide + pattern[i + 1:]
                    mutation_generator(n, m, i, cn, cm, nucleotide, new_pattern, mutated_kmers_list, d)
        mutated_kmers_list.append(pattern)

    else:
        mutated_kmers_list.append(pattern)


def frequent_words_with_mismatch(text, k, d):

    """
    Finds the most frequent k-mers with at most 'd' mismatches in the string 'text'

    :param text:
    :type text: str
    :param k:
    :type k: int
    :param d:
    :type d: int
    :return:
    :rtype: list

    Sample Input:
    ACGTTGCATGTCGCATGATGCATGAGAGCT
    4 1

    Sample Output:
    GATG ATGC ATGT
    """
    kmers = {}
    mutated_kmers = {}
    mutated_kmers_list = []

    max_frequency = 0
    most_frequent_kmers = set()

    for i in range(0, len(text) - k + 1):
        kmer = text[i:i + k]
        if kmer not in kmers:
            kmers[kmer] = 1
        else:
            kmers[kmer] += 1

    for kmer in kmers.keys():
        mutation_generator(None, None, None, None, None, None, kmer, mutated_kmers_list, d)
        val = kmers[kmer]
        mutated_kmers[kmer] = mutated_kmers.get(kmer, 0) + val

        for pattern in mutated_kmers_list:
            mutated_kmers[pattern] = mutated_kmers.get(pattern, 0) + val

        del mutated_kmers_list[:]

    for kmer in mutated_kmers:
        frequency = mutated_kmers[kmer]

        if frequency > max_frequency:
            most_frequent_kmers.clear()
            max_frequency = frequency

        if frequency == max_frequency:
            most_frequent_kmers.add(kmer)

    return most_frequent_kmers

in_text = input()
in_k, in_d = map(int, input().split())

print(" ".join(frequent_words_with_mismatch(in_text, in_k, in_d)))