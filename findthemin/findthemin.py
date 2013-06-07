import sys
import heapq

def findthemin(n, k, a, b, c, r):
    # Get the starter array
    array = calculatek(a, b, c, r, k)
    return heapmin(n, k, array)

def basicmin(n, k, array):
    for i in range(k, n):
        new = 0
        while new in array:
            new += 1
        array.append(new)
        del array[0]

    return array[k-1]

def fastermin(n, k, array):

    # First get to a steady state
    top = min(2*k +1, n)
    new = last = 0 
    for i in range(k, top):
        new = min(last, new)
        while new in array:
            new += 1
        array.append(new)
        last = array[0]
        del array[0]
        if new  == k:
            break

    if i <= n-1:
        array = [last] + array
        return array[((n -1 - i) % (k+1)) - 1]
    return array[k-1]

def heapmin(n, k, array):

    heap = heapify(k, array)
    
    # First get to a steady state
    i = k
    while (i == k) or (len(heap) > 1 and i <= n -1):
        #print heap
        minel = heapq.heappop(heap)
        #minel = heap.heappop() 
        array.append(minel)
        last = array[i-k]
        #print last, minel
        if last <= k:
            heapq.heappush(heap, last)
        i += 1
    print array

    return array[((n -1 - i) % (k+1)) - 1 + (i-k)]

def heapify(k, array):
    # Create Heap
    sortedels = range(k+1)
    for i in array:
        if i <= k:
            sortedels[i] = -1
    missing = filter(lambda x: x>=0, sortedels)
    heapq.heapify(missing)
    return missing

def calculatek(a, b, c, r, k):
    '''Gets the inital array'''
    array = [-1]* k
    for i in range(k):
        if i == 0:
            array[i] = a
        else:
            array[i] = (b * array[i-1] + c) % r
        
    return array

if __name__ ==  '__main__':
    filep = open(sys.argv[1])
    m  = int(filep.readline())
    for l in range(m):
        one = filep.readline()
        two = filep.readline()
        n, k = map(int, one.split())
        a, b, c, r = map(int, two.split())
        
        minn = findthemin(n, k, a, b, c, r)
        print 'Case #%d: %s' % (l+1, minn)
