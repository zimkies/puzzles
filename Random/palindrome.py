'''
1) Computes the next highest palindrome number given positive int i:
2) Write a binary search tree checker
'''
import random

def upper_palindrome(n):
    '''
    Computes the next highest palindrome number given positive int i:
    '''
    en = map(int, str(n))
    last = len(en) -1
    start_left = left = int(last/2)
    start_right = right = last - left
    over = False
    while (right <= last):
        # If right is lower than left equalize right toleft
        if en[right] < en[left] or over:
            en[right] = en[left]
            over=True
        # If right is bigger than left then restart and increment starting left
        elif en[right] > en[left]:
            en[start_left] += 1
            en[start_right] = en[start_left] 
            left = start_left
            right = start_right
            over = True
            continue

        # Otherwise keep going on
        right += 1
        left -= 1
    print reduce(lambda a, x: a + str(x), en, '')

def bin_search_tree(tree):
    '''Takes a tree and determins whether or not it is a binary search tree'''
    return is_good_branch(tree, None, None)

def is_good_branch(tree, left, right):
    '''Helper function for bin_search_tree. Determines if '''
    if tree is None:
        return True
    if left and tree.val < left: 
        return False
    if right and tree.val > right:
        return False
    return is_good_branch(tree.left, left, tree.val) and is_good_branch(tree.right, tree.val, right) 

class Tree():
    left = None
    right = None
    val = None
    
    def __init__(self, val, left=None, right=None):
        self.left=left
        self.right = right
        self.val = val

tree1 = Tree(1)
tree3 = Tree(3) 
tree2 = Tree(2, tree1, tree3) 
tree4 = Tree(4, tree2) 

tree6 = Tree(6) 
tree8 = Tree(8) 
tree7 = Tree(7, tree6, tree8) 

tree5 = Tree(5, tree4, tree7) 
