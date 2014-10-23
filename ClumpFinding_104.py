__author__ = 'Reza'


def clump_finding(text, k, L , t):

    """
    We defined a k-mer as a "clump" if it appears many times within a short interval of 'text'. More formally,
    given integers 'L' and 't', a k-mer forms an (L, t)-clump inside a (larger) string 'text' if there is an interval
    of the 'text' of length 'L' in which this k-mer appears at least 't' times. (This definition assumes that the
    k-mer completely fits within the interval.)

    :param text:
    :type text: str
    :param k:
    :type k: int
    :param L:
    :type L: int
    :param t:
    :type t: int
    :return:
    :rtype: set

    Sample Input:
    CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA
    5 50 4

    Sample Output:
    CGACA GAAGA
    """
    
    # All possible k-mers:
    kmers = {}
    frequent_kmers = set()

    for i in range(0, len(text) - k + 1):
        pattern = text[i:i + k]

        if pattern not in kmers:
            kmers[pattern] = [i]
        else:
            kmers[pattern].append(i)
            pattern_frequency = len(kmers[pattern])
            if pattern_frequency >= t:
                if (kmers[pattern][-1] - kmers[pattern][pattern_frequency - t]) <= (L - k):
                    frequent_kmers.add(pattern)

    return frequent_kmers

input_text = input()
input_k, input_L, input_t = map(int, input().split(' '))

print(len(clump_finding(input_text, input_k, input_L, input_t)))