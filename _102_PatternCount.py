__author__ = 'Reza Moradi'


def pattern_count(text, pattern):

    """
    This function counts the number of times that a k-mer 'pattern' appears as a substring of 'text'

    :param str text:
    :param str pattern:
    :return:
    :rtype: int

    Sample Input:
    text: GCGCG
    pattern: GCG

    Sample Output:
    2
    """

    counter = 0
    k = len(pattern)

    for i in range(len(text) - k + 1):
        if text[i:i + k] == pattern:
            counter += 1

    return counter

if __name__ == "__main__":

    input_text = input("Enter text: ").upper()
    input_pattern = input("Enter pattern: ").upper()

    print("\nThe result is: ", pattern_count(input_text, input_pattern))