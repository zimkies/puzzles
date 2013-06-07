#!/usr/bin/python

""" breathalyzer """
import sys
import numpy

def breathalyzer(filename, dictionary_name):
    """Prints the score of a wallpost"""
    file = open(filename)
    post = file.read().split()#reduce(lambda l,x: l + x.strip().split(), file.readlines(), [])
    
    dictfile = open(dictionary_name)
    dictionary = dictfile.read().split()#map(lambda x:  x.strip(), dictfile.readlines())
    dict = {}
    for w in dictionary:
        dict[w] = 0
    print "loaded data and dictionary"
    
    print len(dictionary), len(post)
    dist = 0
    for word in post:
            dist += mindistance(word, dictionary)
    
    print dist
    
def mindistance(word, dictionary):
    #Make sure to add base case of empty word
    if dictionary.has_key(word):
        return dictionary[word]

def distance(w1, w2, dict):
    """Calculates the distance between 2 words"""
    l1 = len(w1)
    l2 = len(w2)
    matrix = numpy.zeros((l1 +1, l2 + 1), "int")
    
    # fill matrix
    matrix[1,:] = 1
    matrix[:,1] = 1
    matrix[0,0] = 0
    
    for i in range(1,l1+1):
        for j in range(1,l2+1):
    
            if (w1[i-1] == w2[j-1]):
                d = 0
            else:
                d = 1
            matrix[i,j] = min( matrix[i-1,j-1] + d,
                         matrix[i-1, j] + 1,
                         matrix[i, j-1] + 1)
    
    return matrix[l1,l2]
#def distance(w1, w2):
#    """Calculates the distance between 2 words"""
#    l1 = len(w1)
#    l2 = len(w2)
#    matrix = numpy.zeros((l1 +1, l2 + 1), "int")
#    
#    # fill matrix
#    matrix[1,:] = 1
#    matrix[:,1] = 1
#    matrix[0,0] = 0
#    
#    for i in range(1,l1+1):
#        for j in range(1,l2+1):
#    
#            if (w1[i-1] == w2[j-1]):
#                d = 0
#            else:
#                d = 1
#            matrix[i,j] = min( matrix[i-1,j-1] + d,
#                         matrix[i-1, j] + 1,
#                         matrix[i, j-1] + 1)
#    
#    return matrix[l1,l2]

    
if __name__ == "__main__":
    # Usage
    if (len(sys.argv) != 2):
        sys.exit("Usage: ./breathalyzer inputfile")
    dictionary_file = "dictionary.txt" #"/var/tmp/twl06.txt""smalldictionary.txt"
    breathalyzer((sys.argv[1]), dictionary_file)
