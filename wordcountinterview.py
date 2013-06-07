import re
import string

def foo(filename):
    count = {}
    for line in open(filename):
        words = line.strip().split(' ')
        for rawword in words:
            word = word.lower()
            count[word] = count.get(word, 0) + 1 
    return count


def main(filename, common_words=None):
    count = foo(filename)
    
    if common_words:
        common = map(lambda x: x.strip(), open(common_words).readlines())
        for c in common:
            c = c.lower()
            if count[c]:
                del count[c]

    for k, v in count.iteritems():
        print "%s: %d" % (k, v)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        exit('usage: foo filename badwordsfilename')
    file1name = sys.argv[1]
    file2name = sys.argv[2]
    main(file1name, file2name)
