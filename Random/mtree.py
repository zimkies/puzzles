'''
My defined Tree Class
'''

class tree:
    
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children
        
    def is_leaf(self):
        if len(self.children) == 0:
            return True
        else:
            return False
