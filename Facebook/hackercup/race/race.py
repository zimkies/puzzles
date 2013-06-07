
import sys
import math
import numpy
import fractions

def racer(array):
    opponents = int(array[0])
    turns = int(array[1])
    probs = []
    for i in range(2, 2*turns+1, 2):
        probs.append((int(array[i]), int(array[ i+1])))
    
    solution = [probs[:opponents-1],[]]
    
    probs.sort(cmp=comparison, reverse=True)
    total = 1
    for i in range(turns):
        if (i < opponents -1):
            q = fractions.Fraction(1, probs[i][0])
        else:    
            q = fractions.Fraction(1, probs[i][1])
        p = 1-q
        total*=p
        
    return total
def comparison(a,b):
    aover = 1-fractions.Fraction(1,a[0])
    asafe = 1-fractions.Fraction(1,a[1])
    bover = 1-fractions.Fraction(1,b[0])
    bsafe = 1-fractions.Fraction(1, b[1])
    if (aover*bsafe < bover*asafe):
        return -1
    if (aover*bsafe > bover*asafe):
        return 1
    if (aover*bsafe == bover*asafe):
        return 0
    
    
    
def race(filename):
    
    f = open(filename)
    n = int(f.readline())
    for i in range(n):
        r = racer(f.readline().split())
        
        #for j in range(int(nums[0])):
        #    nums.append(f.readline().split()[0])
        ##f.readline()
        #nums.append(string)
        #print nums
       # map = Map(nums)
        #map.print_maze()
        ##ath = dijkstras.shortestPath(map.graph, map.start, map.end)
        print r

if __name__ == "__main__":
    # Usage
    if (len(sys.argv) > 3):
        sys.exit("Usage: round1 nputfile option")
    
    # Which option?
    race(sys.argv[1])