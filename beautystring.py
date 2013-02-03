import sys
import operator

def max_beauty(string):
    beauty = 0

    # Dictionarize it
    counts = {}
    for l in string:
        if l.isalpha():
            counts[l.lower()]  = counts.get(l.lower(), 0) + 1
        
    # Create sorted list
    sortedcounts = sorted(counts.itervalues(), reverse=True)

    # Iterate through list and add value
    currentval = 26
    for i in sortedcounts:
        beauty += currentval*i
        currentval -= 1

    return beauty

       

    return 5

if __name__ ==  '__main__':
    filep = open(sys.argv[1])
    m  = int(filep.readline())
    for i, line in enumerate(filep):
        string = line
        beauty = max_beauty(string)
        print 'Case #%d: %d' % (i+1, beauty)
