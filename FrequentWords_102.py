__author__ = 'Reza Moradi'

input_text = input("Enter text: ").upper()
input_k = int(input("Enter k: "))


def frequent_words(text, k):

    """
    This function finds the most frequent k-mers in a text

    Sample Input:
    text: ACGTTGCATGTCGCATGATGCATGAGAGCT
    k: 4

    Sample Output:
    CATG GCAT
    """

    # All possible k-mers with their frequency will be stored in this set:
    kmers = {}

    # Frequency of most frequent k-mer:
    max_freq = 0

    # Most frequent k-mers will be stored in this list:
    max_kmers = []

    for i in range(len(text) - k + 1):
        # Creating a k-mer
        sub_text = text[i:i + k]

        # Updating 'kmers' database for 'sub_text'
        if sub_text not in kmers:
            kmers[sub_text] = 1

        else:
            kmers[sub_text] += 1

        # Checking if 'sub_text' is more frequent than k-mers in 'max_kmers'. If so, replace 'sub_text' with all
        # those kmers. If 'sub_text' is as frequent as those k-mers, add it to the list.
        freq = kmers[sub_text]

        if freq > max_freq:
            del max_kmers[:]
            max_freq = freq
            max_kmers.append(sub_text)

        elif freq == max_freq:
            max_kmers.append(sub_text)

    max_kmers.sort()

    return max_kmers

print("\nThe result is:", " ".join(frequent_words(input_text, input_k)))