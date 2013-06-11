
import sys
import math
import numpy
import dijkstras

def racer(array):
    opponents = array[0]
    turns = array[1]
    probs = []
    for i in range(2, 2*turns+1, 2):
        probs.append((array[i], array[ i+1]))
    probs.sort()
    total = 1
    for i in range(opponents):
        q = fraction.Fraction(1, probs[i][0])
        p = 1-q
        total*=p
    for i in range(turns-opponents):
        q = fraction.Fraction(1, probs[i][1])
        p = 1-q
        total*=p
        
    return total
    
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