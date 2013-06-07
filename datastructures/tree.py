from collections import deque

class Tree():
    depth  = None
    """My own instance of a tree"""
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.depth = self.get_depth()

    def printout(self):
        treedepth = self.get_depth()
        list = deque([(self,treedepth)])
        depth = treedepth + 1
        while (len(list) >0):
            t = list.popleft()
            d = t[1]
            t = t[0]
            
            # break if bottom row is reached
            if (d <= 0):
                break
            
            # append children to list
            if ((t is None) or (t.left is None)):
                list.append((None, d-1))
            else:
                list.append((t.left, d -1))
            if ((t is None) or (t.right is None)):
                list.append((None, d-1))
            else:
                list.append((t.right, d -1))
                    
            if (t is None):
                val = '*'
            else:
                val = t.val
                    
                    
            if (d<depth):
                depth = d
                print "\n"
                lineprint(val, d)
            else:
                print "-",
                lineprint(val, d)
            

    def get_depth(self):
        if self.depth is not None:
            return self.depth
        else:
            if (self.left is None):
                l = 0
            else: l = self.left.get_depth()
            
            if (self.right is None):
                r = 0
            else: r = self.right.get_depth()
            
            self.depth = max(l, r) + 1
            return self.depth
                    
    def set_left(self, tree):
        self.left = tree
        self.get_depth()
            
    def set_right(self, tree):
        self.right = tree
        self.get_depth()

def lineprint(val, depth):
	h  = 2**depth - 1
	for i in range(h):
		print "-",
	print val,
	for i in range(h):
		print "-",
		
def mytree():
	a = Tree(1)
	b = Tree(2)
	c = Tree(3)
	d = Tree(4)
	e = Tree(5)
	f = Tree(6, a)
	g = Tree(7, c, d)
	h = Tree(8, f,g)
	i = Tree(9, h, f)
	j = Tree(0, h)
	return h,i, j

def bsort(ints):
	list = []
	for i,int in enumerate(ints):
		list[i] = [int]
	
	

class Heap(Tree):
	
	def __init__(self, vals):
		self.heap = Emptytree()
		for v in vals:
			self.insert(v)
		self.depth = self.get_depth()
	
	def insert(self, x, heap=None):
		
	def get_max(self):
		val = self.tree.val
		l = self.tree.left
		r = self.tree.right
		
		if (isinstance(l, Emptytree)):
			self.tree = r
		elif (isinstance(r, Emptytree)):
			self.tree = l
		#elif (index(l.val) > index(r.val)):
			
def heap_insert(val, heap):
	
	# if heap is empty, return a tree
	if isinstance(heap, Emptytree):
		return Tree(val)
	
	l = self.tree.left
	r = self.tree.right
	
	if (isinstance(l, Emptytree)):
		self.tree = r
	elif (isinstance(r, Emptytree)):
		self.tree = l
	

def merge_sort(lst):
	l = len(lst)
	a = lst[:l/2]
	b = lst[l/2:]
	if (len(a) == 0):
		return b
	elif len(b) == 0:
		return a
	return merge(merge_sort(a), merge_sort(b))
	
def merge(a,b):
	al = len(a)
	bl = len(b)
	s = []
	ai,bi = 0,0
	while ((ai < al) and (bi < bl)):
		if a[ai] > b[bi]:
			s.append(b[bi])
			bi +=1
		else:
			s.append(a[ai])
			ai +=1
			
	s.extend(a[ai:])
	s.extend(b[bi:])
	return s