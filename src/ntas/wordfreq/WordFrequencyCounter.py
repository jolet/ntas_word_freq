'''
Created on 19. lip 2016.

@author: jk
'''
from BinaryTree import *
from Utils import *
from Reader import read_docx

###########################[WORD_FFREQUENCY_CALCULATOR]##############################

document_text = read_docx('../resources/Homer2.docx')
frequencyBST = BinaryTree()

for word in document_text.split():
    # print (normalizeWord(word))
    normalizedWord = normalizeWord(word).encode('utf-8').strip().upper()
    createAndInsertNode(frequencyBST, normalizedWord)    
    
print '========================[UNIQUE WORDS INORDER]======================\n'
inorder_string_list = frequencyBST.inorder_as_string().split()
print 'unique words found: ' + str(len(inorder_string_list))
print_as_table(inorder_string_list, False)

print '\n\n---------------------[WORDS BY FREQUENCY]------------------------'
inorder_with_frequency = frequencyBST.inorder_with_frequency([])
inorder_with_frequency.sort(key=lambda tup: tup[0], reverse=True)
print_as_table(inorder_with_frequency, True)
