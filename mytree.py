from collections import deque

class Emptytree:
	"""My own instance of a tree"""
	def __init__(self):
		print "empty tree"

	def get_depth(self):
		return 0
	def get_size(self):
		return 0
		
class Tree():
	depth  = None
	children = None
	"""My own instance of a tree"""
	def __init__(self, val, left=None, right=None):
		if (left==None):
			left = Emptytree()
		if (right==None):
			right = Emptytree()
		self.val = val
		self.left = left
		self.right = right
		self.update()

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
			if ((t is None) or isinstance(t.left, Emptytree)):
				list.append((None, d-1))
			else:
				list.append((t.left, d -1))
			if ((t is None) or isinstance(t.right, Emptytree)):
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
			self.depth = max(self.left.get_depth(), self.right.get_depth()) + 1
			return self.depth
	
	def get_size(self):
		if self.size is not None:
			return self.size
		else:
			self.size = self.left.get_size() + self.right.get_size() + 1
			return self.size
	def update(self):
		self.depth = max(self.left.get_depth(), self.right.get_depth()) + 1
		self.size = self.left.get_size() + self.right.get_size() + 1
		
	
	def set_left(self, tree):
		self.left = tree
		self.update()
		
	def set_right(self, tree):
		self.right = tree
		self.update()

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
	
	
class Emptyheap():
	"""My own instance of a heap"""
	def __init__(self):
		print "empty heap"

	def get_depth(self):
		return 0
	
class Heap():
	
	def __init__(self, vals):
		self.heap = Emptytree()
		for v in vals:
			self.insert(v)
	
	def insert(self, x):
		self.heap = heap_insert(x, self.heap)
		
	def get_max(self):
		val = self.heap.val
		l = self.heap.left
		r = self.heap.right
		
		if (isinstance(l, Emptytree)):
			self.heap = r
		elif (isinstance(r, Emptytree)):
			self.heap = l
		#elif (index(l.val) > index(r.val)):
	

def heap_insert(val, heap):
	
	t = Tree(val)
	# if heap is empty, return a tree
	if isinstance(heap, Emptytree):
		return t
	
	# Switch head of heap and val if heap > val
	if heap.val > val:
		t.set_left(heap.left)
		t.set_right(heap.right)
		heap.set_left(Emptytree())
		heap.set_right(Emptytree())
		heap,t = t,heap
	
	l = heap.left
	r = heap.right

	if r.get_size() >= l.get_size():
		heap.set_left(heap_insert(t.val, heap.left))
		return heap
	else:
		heap.set_right(heap_insert(t.val, heap.right))
		return heap
	
def heap_merge(a, b):
	ad = a.get_depth()
	bd = b.get_depth()
	if (ad < bd):
		raise Exception("Left child must always be bigger than right child")
	
	
	t1 = a.left
	if (a.right.get_size() > b.get_size()):
		new = heap_merge(a.right, b)
	else: 
		new = heap_merge(b, a.right)
	
	if (new.get_size() > a.get_size()):
		return Tree(a.val, new, t1)
	else: return Tree(a.val, t1, new)

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