#!/usr/bin/python

""" usrbincrash """
import sys
import numpy

class Good():
    
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = float(weight)
        self.cost = float(cost)
        self.unitcost = self.cost/self.weight

    def __str__(self):
        return  "<Person: " + str((self.name, self.weight, self.cost)) + '>'

def usrbincrash(filename):
    file = open(filename)
    people = map(lambda x: Good(*x.split()), file.readlines())
    numpeople = len(people)
    
    
    
    for p in people_original:
    #    print p.name
    #    print p.closest
    #    print ""
        #print p.closest
        #print tuple(map(lambda x: x[0].name, p.closest))
        print p.name,
        print '%d,%d,%d' % tuple(map(lambda x: x[0].name, p.closest))
    
        
    return
    
if __name__ == "__main__":
    # Usage
    if (len(sys.argv) != 2):
        sys.exit("Usage: usrbincrash inputfile")
    usrbincrash((sys.argv[1]))
