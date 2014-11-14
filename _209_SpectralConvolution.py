__author__ = 'Reza Moradi'


def spectral_convolution(spectrum):
    """
    Compute the convolution of 'spectrum'.

    :param spectrum:
    :type spectrum: list
    :return:
    :rtype: list

    Sample Input:
    0 137 186 323

    Sample Output:
    137 137 186 186 323 49
    """

    spectrum_length = len(spectrum)
    convolution = []

    for i in range(spectrum_length):
        for j in range(i + 1, spectrum_length):
            convolution.append(abs(int(spectrum[i]) - int(spectrum[j])))

    return convolution

if __name__ == "__main__":

   print(" ".join(map(str, sorted(spectral_convolution(spectrum=input().split(' '))))))
    #
    # print('\n', len(convolution))