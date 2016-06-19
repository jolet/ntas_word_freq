'''
Created on 19. lip 2016.

@author: josip.kovacek
'''
# python-docx 
from docx import Document
# debug mode
# import pdb
# pdb.set_trace()

# Predstavlja binarno stablo
class Tree:
    def __init__(self, root = None, left = None, right = None):
        self.root = root
        self.left = left
        self.right = right
        self.frequency = 0
        return
    
    def inorder(self):
        temp_inorder=''
#         temp_inorder_arr=[]
        # navigate left tree
        if self.left != None:
            if temp_inorder:
                temp_inorder += " " 
            temp_inorder = temp_inorder + self.left.inorder()
        
        # navigate ROOT
        if temp_inorder:
            temp_inorder += " "
        if self.root:
            temp_inorder += self.root
        
        # navigate right tree
        if self.right != None:
            if temp_inorder:
                temp_inorder += " "
            temp_inorder = temp_inorder + self.right.inorder()
        
        return temp_inorder  
    
    def inorder_instant_print(self):
        # navigate left tree
        if self.left != None:
            self.left.inorder_instant_print()
        
        # navigate ROOT
        #if self.root != None:
        print self.root,
        
        # navigate right tree
        if self.right != None:
            self.right.inorder_instant_print()

# Kreira novi node i dodaje ga u binarno uredjeno stablo # from Tree import *
def createAndInsertNode(tree_ref, word):

    word_node_ref = Tree(word)
    if tree_ref.root == None:
        tree_ref.root = word_node_ref.root 
    else: 
        added = False
        while not added:
            if word <= tree_ref.root:
                if word == tree_ref.root:
    #                 print "same word: " + word
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
    #         else: 
    #             tree_ref.frequency += 1;
    #             print 'found duplicate'
                        
    #return tree_ref

# Uklanja interpunkcije iz rijeci
def normalizeWord(word):
    #out = stringIn.translate(stringIn.maketrans("",""), string.punctuation)
    return "".join(char for char in word if char not in ('!','.',',','?','(', ')', '"', '-', ':', ";"))

###########################[WORD_FFREQUENCY_CALCULATOR]##############################
print("Starting word frequency calculation...")
document = Document('Homer2.docx')
frequencyBST = Tree()

for paragraph in document.paragraphs:
        for word in paragraph.text.split():
            print (normalizeWord(word))
            normalizedWord = normalizeWord(word).encode('utf-8').strip().upper()
            #frequencyBST = 
            createAndInsertNode(frequencyBST, normalizedWord)

print "============================[INORDER]=========================\n"
ino = frequencyBST.inorder().split()
print 'unique words: ' + str(len(ino))
for idx, val in enumerate(ino):
    if idx % 7 == 0:
        print "\n"
    print '{:>4d}. {:15}'.format(idx + 1, val),
print '\n------------------------------------------------------------------\n'
frequencyBST.inorder_instant_print()    
