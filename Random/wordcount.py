import re
import string

def wordcount(filename):
    '''Returns a dictionary of wordcounts in file'''
    count = {}
    pattern = re.compile('[\W_]+')
    for line in open(filename):
        words = line.strip().split(' ')
        for rawword in words:
            word = pattern.sub('', rawword).lower()
            count[word] = count.get(word, 0) + 1 
    return count


def main(filename, common_words=None):
    '''Prints out word counts from a file, removing common words
    The common word file (if supplied) should have one word per line'''
    count = wordcount(filename)
    
    # Delete common words
    if common_words:
        common = map(lambda x: x.strip(), open(common_words).readlines())
        for c in common:
            c = c.lower()
            if count[c]:
                del count[c]

    # Print out results
    for k, v in count.iteritems():
        print "%s: %d" % (k, v)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        exit('usage: wordcount filename badwordsfilename')
    filename = sys.argv[1]
    common_words = sys.argv[2]
    main(filename, common_words)
