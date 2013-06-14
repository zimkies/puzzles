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

def distance(w1, w2):
    """Calculates the Levenshtein distance between 2 words"""
    l1 = len(w1)
    l2 = len(w2)
    matrix = numpy.zeros((l1 +1, l2 + 1), "int")

    # fill matrix
    for i in range(l1+1):
        matrix[i, 0] = i
    for j in range(l2+1):
        matrix[0, j] = j

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


_end = "_end"
class Trie(object):
    '''A Trie Class'''

    def __init__(self, words):
        self.root = {}
        self.words = words

        self.insertwords(words)

    def insertwords(self, words):
        '''Inserts words into root'''
        for w in words:
            self.insertword(w, self.root)

    def insertword(self, word, node):
        '''Inserts a word into node'''
        for c in word:
            node = node.setdefault(c, {})

        node[_end] = word

    def search(self, word, node=None):
        if node is None:
            node = self.root
        for c in word:
            if not node.get(c):
                return False
            node = node.get(c)
        return bool(node.get(_end))

    def close_matches(self, word, dist=2, node=None):
        return self.closest_match_helper(word, node=self.root, dist=dist)

    def closest_match_helper(self, word, node, dist):
        '''
        NOTE we refer to edit/delete/insert as actions on the main word
        '''
        # print word, dist
        # Case where dist is -1
        if dist < 0:
            return False

        # Case where word is empty and trie ends (means they match)
        if not word and node.get(_end):
            # Fixme return full word
            print node.get(_end), dist
            return True

        # How about if just word is empty but trie doesn't end
        if not word:
            # Return length of trie from here
            found = False
            for k in node.keys():
                # Insert
                found = self.closest_match_helper(k + word, node, dist -1) or found
            return found

        # Iterate over keys for keep, edit, and insert
        found = False
        for k in node.keys():

            # if this key is the character we want, recurse with same distance
            if k == word[0]:
                found = self.closest_match_helper(word[1:], node.get(k), dist) or found

            elif k == _end:
                pass

            # Otherwise  we do an edit
            else:
                # Edit
                found = self.closest_match_helper(word[1:], node.get(k), dist-1) or found

            # Insert
            found = self.closest_match_helper(k + word, node, dist -1) or found

        # Try a Delete not matter what:
        return self.closest_match_helper(word[1:], node, dist-1) or found

def triebreathalyzer(filename, dictionary_name):
    file = open(filename)
    post = file.read().split()

    dictfile = open(dictionary_name)
    dictionarylist = dictfile.read().split()
    print "loaded data and dictionarylist"
    print len(dictionarylist), len(post)
    dist = 0
    wordstrie = Trie(map(lambda x: x.lower(), dictionarylist))

    for word in post:
        print 'searching ', word.lower()
        i = 0
        while 1:
            matches = wordstrie.close_matches(word.lower(), i)
            if matches:
                print "matched", matches, i
                break
            i += 1

        dist += i

    print dist



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


if __name__ == "__main__":
    # Usage
    if (len(sys.argv) != 2):
        sys.exit("Usage: ./breathalyzer inputfile")
    dictionary_file = "dictionary.txt" #"/var/tmp/twl06.txt""smalldictionary.txt"
    #breathalyzer((sys.argv[1]), dictionary_file)
    triebreathalyzer((sys.argv[1]), dictionary_file)
