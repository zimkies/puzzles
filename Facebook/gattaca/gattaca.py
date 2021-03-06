#!/usr/bin/python

# This version passes the Facebook timing test at 3579.704 ms
""" gataca """
import sys
#import numpy
class Sequence():
    
    def __init__(self, start, stop, score):
        self.start = start
        self.stop = stop
        self.score = score

def gataca(filename):
    """Prints the optimal score of DNA predictions"""
    file = open(filename)
    dnalength = int(file.readline())
    
    # The DNA
    for i in range(int(ceiling(dnalength/80.0))): file.readline()
    
    # Collect sequence data
    seqlength = int(file.readline())
    sequences = {}
    dna = [0]*(dnalength +1)#numpy.zeros(dnalength + 1, int) #add a one so that index -1 gives a 0
    
    # Store the sequences
    for i in range(seqlength):
        start, stop, score = file.readline().split()
        lst = sequences.setdefault(stop, [])
        lst.append(Sequence(int(start), int(stop), int(score)))
    
    for i in range(dnalength):    
        scores = [dna[i-1]]
        if sequences.has_key(str(i)):
            for seq in sequences[str(i)]:
                scores.append(dna[seq.start -1] + seq.score)
                
        dna[i] = max(scores)

    print dna[dnalength-1]
    
    file.close()
    return
    
def ceiling(number):
    if (int(number)<number):
        return int(number+1)
    else:
        return int(number)
        
    
    
    
if __name__ == "__main__":
    # Usage
    if (len(sys.argv) != 2):
        sys.exit("Usage: gataca inputfile")
    gataca((sys.argv[1]))
    
