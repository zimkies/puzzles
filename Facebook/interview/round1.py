## Facebook first round interview

# jerry@fb.com
#
#                     45
#          34                     16
#      22                    15         10
#         8                     11     6
#        5                     7      1 4
#      
# Cartesian tree: every node is greater than its children. Every number is unique
# 22 5 8 34 45 15 7 11 16 1 6 4 10

def inorderToCartesianTree(inorder):
    return inorderToCartesianTreeRec(inorder, 0, len(inorder) - 1)
            
def inorderToCartesianTreeRec(inorder, left, right):
     
    # base case:
    if left > right:
        return None
       
    # Get the maximum element in the current range
    Max = (left, 0)
    for i in range(left, right+1):
        if inorder[i] > Max[1]:
            Max = (i, inorder[i])
    
    leftnode = inorderToCartesianTreeRec(inorder, left, Max[0]-1)
    rightnode = inorderToCartesianTreeRec(inorder, Max[0]+1, right)
    return (leftnode, Max[1], rightnode)
    
# removeClass('top middle bottom bottom-right gray invisible happy bottom', 'bottom')
#   -> 'top middle bottom-right gray invisible happy'

# remove the word roRemove from the string original
def removeClass(original, toRemove):
    lst = original.split()
    ls2 = filter(lambda x: x==toRemove, original)
    return reduce(lambda w,x: w+x, ls2, '')
    