#!/usr/bin/python

""" round 1"""
import sys
import math
import numpy

def dsquares(filename):
    max = 2147483647
    f = open(filename)
    n = int(f.readline())
    xs = []
    for i in range(n):
        xs.append(int(f.readline()))
    ints = range(int(math.sqrt(max)) +2)
    squares = map(lambda x: x**2, ints)
    for x in xs:
        count = 0
        for s in squares:
            remainder = x-s
            if (remainder < 0):
                break;
            if ((issquare(remainder)) and (s >=  remainder)):
                count +=1
        print count
        
    
def issquare(n):
    s = math.sqrt(n)
    if (int(math.floor(s)) == int(math.ceil(s))):
        return True
    else:
        return False

class Peggame():
    
    def __init__(self, data):
        
        self.rows = int(data[0])
        self.cols = int(data[1])*2-1
        self.target = int(data[2])
        self.board = numpy.zeros((self.rows, self.cols), int)
        for r in range(self.rows):  
            for c in range(self.cols):
                if (((c+r) %2) == 0):
                    self.board[r,c] = 1
        for i in range(int(data[3])):
            r = int(data[2*i + 4])
            c = int(data[2*i + 5])*2-1
            if (r%2==1):
                c+=2
            self.board[r,c] = 0

        self.props = numpy.zeros((self.rows+1,self.cols)) - 1
        self.props[self.rows] = 0
        self.props[self.rows, 2*self.target+1] = 1
        
    def lookup(self, r, c):
        
        if (self.props[r,c] != -1):
            return self.props[r,c]
        elif (self.board[r,c] == 0):
            self.props[r,c] = self.lookup(r+1,c)
        elif(((r%2==0) and (c==0)) or ((r%2==1) and (c==1))):
            self.props[r,c] = self.lookup(r+1,c+1)
        elif(((r%2==0) and (c==self.cols-1)) or ((r%2==1) and (c==self.cols-1))):
            self.props[r,c] = self.lookup(r+1,c-1)
        else:
            self.props[r,c] = 0.5*self.lookup(r+1, c+1) + 0.5*self.lookup(r+1, c-1)
        return self.props[r,c]
    
    def maximum(self):
        best = (1, 0)
        for i in range(1, self.cols, 2):
            p = self.lookup(0,i)
            if (p> best[1]):
                best = (i/2, p)
        #print self.board
        #print self.props 
        return best
    
def peg(filename):
    f = open(filename)
    n = int(f.readline())
    games = []
    for i in range(n):
        p = Peggame(f.readline().split())
        print "%d %.6f" % p.maximum()



def lexi(filename):
    f = open(filename)
    n = int(f.readline())
    words = []
    for i in range(n):
        words.append(f.readline().split()[1:])
    for w in words:
        w.sort()
        print reduce(lambda s, x: s+x, w, '')

if __name__ == "__main__":
    # Usage
    if (len(sys.argv) > 3):
        sys.exit("Usage: round1 nputfile option")
    
    dict = {"dsquares": dsquares, "peg": peg, "lexi": lexi}
    # Which option?
    dict[sys.argv[2]](sys.argv[1])