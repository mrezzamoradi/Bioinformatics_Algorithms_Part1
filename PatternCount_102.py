__author__ = 'Reza Moradi'

# This code counts the number of times that a k-mer Pattern appears as a substring of Text
#
# Sample Input:
#   GCGCG
#   GCG
#
# Sample Output:
#   2

text = input("Enter text: ").upper()
pattern = input("Enter pattern: ").upper()

counter = 0
k = len(pattern)

for i in range(len(text) - k + 1):
    if text[i:i + k] == pattern:
        counter += 1

print("\nThe result is: ", counter)