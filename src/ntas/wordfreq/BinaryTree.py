'''
Created on 20. lip 2016.

@author: jk
'''
# Binary tree
class BinaryTree:
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right
        self.frequency = 1
        return
    
    def inorder_as_string(self):
        temp_inorder = ''
        # navigate left tree
        if self.left != None:
            if temp_inorder:
                temp_inorder += " " 
            temp_inorder = temp_inorder + self.left.inorder_as_string()
        
        # navigate ROOT
        if temp_inorder:
            temp_inorder += " "
        if self.root:
            temp_inorder += self.root
        
        # navigate right tree
        if self.right != None:
            if temp_inorder:
                temp_inorder += " "
            temp_inorder = temp_inorder + self.right.inorder_as_string()
        
        return temp_inorder  
    
    def inorder_with_frequency(self, inorder_list):
#         inorder_list = []
        # navigate left tree
        if self.left != None:
            self.left.inorder_with_frequency(inorder_list)
        
        # navigate ROOT
        # if self.root != None:
        if self.root :
            inorder_list.append((self.frequency, self.root))
            # print '|{:2}. {:5}'.format(self.frequency, self.root),

        # navigate right tree
        if self.right != None:
            self.right.inorder_with_frequency(inorder_list)
            
        return inorder_list

# Creates new node and inserts it into binary tree
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
