'''
Created on 19. lip 2016.

@author: jk
'''
# python-docx 
from docx import Document

# Predstavlja binarno stablo
class BinaryTree:
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right
        self.frequency = 1
        return
    
    def inorder_instant_print(self):
        # navigate left tree
        if self.left != None:
            self.left.inorder_instant_print()
        
        # navigate ROOT
        if self.root :
            print '|{:2}. {:5}'.format(self.frequency, self.root),

        # navigate right tree
        if self.right != None:
            self.right.inorder_instant_print()

# Kreira novi node i dodaje ga u binarno uredjeno stablo # from BinaryTree import *
def createAndInsertNode(tree_ref, word):

    word_node_ref = BinaryTree(word)
    if tree_ref.root == None:
        tree_ref.root = word_node_ref.root 
    else: 
        added = False
        while not added:
            if word <= tree_ref.root:
                if word == tree_ref.root:
                    # print "same word: " + word
                    tree_ref.frequency += 1
                    return tree_ref
                if tree_ref.left == None:
                    tree_ref.left = word_node_ref
                    added = True
                else:
                    tree_ref = tree_ref.left
            
            elif word > tree_ref.root:
                if tree_ref.right == None:
                    tree_ref.right = word_node_ref
                    added = True
                else:
                    tree_ref = tree_ref.right

# Uklanja interpunkcije iz rijeci
def normalizeWord(word):
    # out = stringIn.translate(stringIn.maketrans("",""), string.punctuation)
    return "".join(char for char in word if char not in ('!', '.', ',', '?', '(', ')', '"', '-', ':', ";")).encode('utf-8').strip().upper()

###########################[WORD_FFREQUENCY_CALCULATOR]##############################
document = Document('Homer2.docx')
frequencyBST = BinaryTree()

for paragraph in document.paragraphs:
        for word in paragraph.text.split():
            createAndInsertNode(frequencyBST, normalizeWord(word))

print "============================[INORDER]=========================\n"
frequencyBST.inorder_instant_print()    
