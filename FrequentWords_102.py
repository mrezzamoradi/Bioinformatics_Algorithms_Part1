__author__ = 'Reza Moradi'

# This code finds the most frequent k-mers in a string
#
# Sample Input:
#   ACGTTGCATGTCGCATGATGCATGAGAGCT          (string)
#   4                                       (k)
# 
# Sample Output:
#   CATG GCAT

text = input("Enter text: ").upper()
k = int(input("Enter k: "))

# All possible k-mers with their frequency will be stored in this set:
kmers = {}

# Frequency of most frequent k-mer:
maxFreq = 0

# Most frequent k-mers will be stored in this list:
maxKmers = []

for i in range(len(text) - k + 1):
    # Creating a k-mer
    subText = text[i:i + k]

    # Updating 'kmers' database for 'subText'
    if subText not in kmers:
        kmers[subText] = 1

    else:
        kmers[subText] += 1

    # Checking if 'subText' is more frequent than k-mers in 'maxKmers'. If so, replace 'subText' with all
    # those kmers. If 'subText' is as frequent as those k-mers, add it to the list.
    freq = kmers[subText]

    if freq > maxFreq:
        del maxKmers[:]
        maxFreq = freq
        maxKmers.append(subText)

    elif freq == maxFreq:
        maxKmers.append(subText)

maxKmers.sort()
print("\nThe result is: ", " ".join(maxKmers))
