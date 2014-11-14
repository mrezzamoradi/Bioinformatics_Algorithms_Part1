__author__ = 'Reza'


def find_pattern(pattern, text):

    """
    Finds all occurrences of 'pattern' in 'text'

    :param text:
    :type text: str
    :param pattern:
    :type pattern: str
    :return:
    :rtype: list

    Sample Input:
    ATAT
    GATATATGCATATACTTCTAGATGCT

    Sample Output:
    [1, 3, 9]
    """

    k = len(pattern)
    return [i for i in range(len(text) - k + 1) if text[i:i + k] == pattern]

if __name__ == "__main__":

    input_pattern = input("Enter pattern: ").upper()
    input_text = input("Enter text: ").upper()

    print("\nThe result is:", " ".join(map(str, find_pattern(input_pattern, input_text))))