__author__ = 'Reza Moradi'


def skew(gnome):

    """
    We define Skew_i(Genome) as the difference between the total number of occurrences of G and the total number of
    occurrences of C in the first i nucleotides of Genome. The skew diagram is defined by plotting Skew_i(Genome)
    (as i ranges from 0 to |Genome|), where Skew_0(Genome) is set equal to zero. This function will return i(s) where
    Skew_i(Gnome) is minimum.

    :param gnome:
    :type gnome: str
    :return:
    :rtype: list

    Sample Input:
    TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT

    Sample Output:
    11 24
    """

    # Set skew_0(gnome) equal to zero
    skew_value = 0

    # Minimum value of 'skew_value'
    minimum = 0

    # Location of the minimum
    minimum_location = []

    # Keep i and skew_i(gnome) for each i, in 'location' and 'skew_array'
    location = []
    skew_array = []

    for i in range(0, len(gnome)):
        # Calculating the 'skew_value'
        if gnome[i] == 'C':
            skew_value -= 1
        elif gnome[i] == 'G':
            skew_value += 1

        # Fining the minimum
        if skew_value < minimum:
            del minimum_location[:]
            minimum = skew_value
        if skew_value == minimum:
            minimum_location.append(i + 1)

        # Keep i and skew_i(gnome), to plot them later if required
        skew_array.append(skew_value)
        location.append(i)

    return minimum_location

input_gnome = input("Enter the genome: ")

print(" ".join(map(str, skew(input_gnome))))