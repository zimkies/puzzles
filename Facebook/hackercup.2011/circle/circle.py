import sys
import numpy

def play(t,k):
    lst = range(1, t+1)
    cur = 1
    while (len(lst) >  1):
        cur = (cur + k)%t + 1
        lst.pop(cur)
    
def circle(filename):
    
    f = open(filename)
    t = int(f.readline())
    for i in range(t):
        t,k = (f.readline().split())
        
        
        #for j in range(int(nums[0])):
        #    nums.append(f.readline().split()[0])
        ##f.readline()
        #nums.append(string)
        #print nums
       # map = Map(nums)
        #map.print_maze()
        ##ath = dijkstras.shortestPath(map.graph, map.start, map.end)
        print t,k

if __name__ == "__main__":
    # Usage
    if (len(sys.argv) > 3):
        sys.exit("Usage: round1 nputfile option")
    
    # Which option?
    circle(sys.argv[1])