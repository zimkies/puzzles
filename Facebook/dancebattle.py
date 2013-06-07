#!/usr/bin/python

""" breathalyzer """
import sys
import numpy

def dancebattle(filename):
    """Prints if you win or lose the game"""
    
    file = open(filename)
    n_dances = int(file.readline())
    if (n_dances == 0):
        sys.exit("Lose")
    
    # Get the history
    n_history = int(file.readline())
    history = [file.readline().split() for i in range(n_history)]
    if (len(history) == 0):
        lastmove = 0
    else:
        lastmove = history[-1][-1]
    history = map(lambda x: tuple(map(int, sorted(x))), history)
    
    matrixhistory = numpy.zeros((n_dances, n_dances), int)
    for h in history:
        matrixhistory[h] = 1
        matrixhistory[tuple(reversed(h))] = 1
    print lastmove
    
    
    print history
    print matrixhistory
    
    outc = outcome(matrixhistory, lastmove, n_dances)
    # Change to winner of overall game:
    if (n_history %2 == 1):
        outc *=-1
    
    if (outc == 1):
        print "Win"
    else:
        print "Lose"
    
def outcome(matrixhistory, lastmove, n_dances):
    print matrixhistory
    outcom = -1 #lose
    for i in range(n_dances):
        if (matrixhistory[lastmove][i] == 0):
            matrixhistory[lastmove][i] = 1
            matrixhistory[i][lastmove] = 1
            outcom = -1*outcome(matrixhistory, i, n_dances)
            matrixhistory[lastmove][i] = 0
            matrixhistory[i][lastmove] = 0
            if (outcom == 1):
                break
    return outcom

if __name__ == "__main__":
    # Usage
    if (len(sys.argv) != 2):
        sys.exit("Usage: ./dancebattle inputfile")
    dancebattle(sys.argv[1])