#!/usr/bin/python
""" breathalyzer """
import sys
import numpy
import random
import pickle

class Node(object):
    '''A node chich contains an element and children,
    each child has a key corresponding to its lvs distance
    from the element'''

    def __init__(self, el):
        self.el = el
        self.children = {}


class BKTree(object):
    '''BKTree for efficent matching of similar words'''
    root = None

    def __init__(self, wordlist):
        self.root = Node(random.choice(wordlist))
        for w in wordlist:
            print "inserting word ", w
            if w != self.root.el:
                self.insert(w)
        print "done with word inserion"

    def insert(self, el):
        '''Insert an element into the tree'''
        ldist = distance(self.root.el, el)
        node = self.root
        while node.children.get(ldist):
            node = node.children.get(ldist)
            ldist = distance(node.el, el)
        node.children[ldist] = Node(el)
        print node.el, el, ldist

    def search(self, query, error):
        '''Returns a list of elements at most error away from query'''
        return self.recursive_match(query, self.root, error)

    def recursive_match(self, query, node, error):
        ldist = distance(node.el, query)
        matches = []
        if ldist <= error:
            matches.append(node.el)
        for d in range(ldist - error, ldist + error+1):
            if node.children.get(d):
                matches += self.recursive_match(query, node.children.get(d), error)

        return matches

def breathalyzer(filename, dictionary_name, storagefile="tree.pickle"):
    """Prints the score of a wallpost"""
    file = open(filename)
    post = file.read().split()#reduce(lambda l,x: l + x.strip().split(), file.readlines(), [])

    dictfile = open(dictionary_name)
    dictionarylist = dictfile.read().split()#map(lambda x:  x.strip(), dictfile.readlines())
    # dictionary = dict((w,0) for w in dictionarylist)
    print "loaded data and dictionarylist"
    print len(dictionarylist), len(post)
    dist = 0
    try:
        with open(storagefile) as f:
            bktree = pickle.load(f)

    except IOError:
        bktree = BKTree(map(lambda x: x.lower(), dictionarylist))
        with open(storagefile, "w") as f:
            pickle.dump(bktree, f)

    # import pdb
    # pdb.set_trace()

    for word in post:
        print 'searching ', word.lower()
        i = 0
        while 1:
            matches = bktree.search(word.lower(), i)
            if matches:
                print "matched", matches[0], i
                break
            i += 1

        dist += i

    print dist

# def mindistance(word, dictionary):
#     #Make sure to add base case of empty word
#     if dictionary.has_key(word):
#         return dictionary[word]

def distance(w1, w2):
    """Calculates the distance between 2 words"""
    l1 = len(w1)
    l2 = len(w2)
    matrix = numpy.zeros((l1 +1, l2 + 1), "int")

    # fill matrix
    for i in range(l1+1):
        matrix[i, 0] = i
    for j in range(l2+1):
        matrix[0, j] = j
    # matrix[1,:] = 1
    # matrix[:,1] = 1
    # matrix[0,0] = 0

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
