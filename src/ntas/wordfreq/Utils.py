'''
Created on 20. lip 2016.

@author: jk
'''
# Creates new word without interpunction characters
def normalizeWord(word):
    # out = stringIn.translate(stringIn.maketrans("",""), string.punctuation)
    return "".join(char for char in word if char not in ('!', '.', ',', '?', '(', ')', '"', '-', ':', ";"))

# prints list data in multiple columns (7)
def print_as_table(data, with_frequencies):
    for idx, val in enumerate(data):
        if idx % 7 == 0:
            print "\n"
        if with_frequencies:
            # (frequency, word)
            print '|({:>1d}) {:15}'.format(val[0], val[1]),  # encode('utf-8')
        else:
            # index, vord
            print '{:>4d}. {:15}'.format(idx + 1, val),
        
