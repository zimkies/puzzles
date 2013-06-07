import sys
import numpy
MAX= 10000000
JUMP = 1000
def play(line):

    v= line[0]
    outputs = map(int, line[1:])
    secrets = range(outputs[0], MAX+1, JUMP)
    valids = []
    for s in secrets:
        # if correct
        #print s, myrand(s)
        #if ((len(outputs) > 1)):
        #    if(myrand(s)[0] == outputs[1]):
        #        print "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
        
        if (valid(s, outputs, 1, len(outputs))):
            valids.append(s)
    if (len(valids) == 0):
        print "Wrong machine"
    elif (len(valids) == 1):
        seed = valids[0]
        for i in range(len(outputs)-1):
            s,seed = myrand(seed)
        for i in range(10):
            s, seed = myrand(seed)
            print s,
    
        print ''
    else:
        print "Not enough observations"

def valid(s, outputs, i, l):
    if (i >= l):
        #print ''
        return True
    
    
    
    newrand, newseed = myrand(s)
    if (outputs[i] == newrand):
        #print s2,
        return valid(newseed, outputs, i+1,l)
    else:
        #print ''
        return False

def myrand(secret):
    secret = (secret * 5402147 + 54321) % 10000001
    return secret % 1000, secret

def slot(filename):
    
    f = open(filename)
    t = int(f.readline())
    for i in range(t):
        line = f.readline().split()
        play(line)
        
        #for j in range(int(nums[0])):
        #    nums.append(f.readline().split()[0])
        ##f.readline()
        #nums.append(string)
        #print nums
       # map = Map(nums)
        #map.print_maze()
        ##ath = dijkstras.shortestPath(map.graph, map.start, map.end)
        
if __name__ == "__main__":
    # Usage
    if (len(sys.argv) > 3):
        sys.exit("Usage: round1 nputfile option")
    
    # Which option?
    slot(sys.argv[1])