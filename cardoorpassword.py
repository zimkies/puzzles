

class Trie(object):
    '''A data structure for fast lookups'''

def perfect_string_finder(numbers, length):


    # for s in strings(numbers, length, [], 0):
    #     print 's', s

    passwords = set([s for s in strings(numbers, length, [], 0)])
    # Iterate over strings
    count = 0
    for s in strings(numbers, numbers**length + (length- 1  ), [], 0):
        #print s
        if is_perfect_string(s,numbers, length, passwords):
            count += 1
            print s

    if not count:
        print "No perfect strings"

def is_perfect_string(s, numbers, length, words):
    words = words.copy()
    for i in range(numbers**length):
        # print s,  s[i:i+length], i, i+length
        if s[i:i+length] in words:
            words.remove(s[i:i+length])
        else:
            return False
            # print "not",s,  s[i:i+length], i, i+length
    return True

def strings(numbers, length, stringlist, depth):
    if depth == length:
        yield reduce(lambda a, b: a+str(b), stringlist, "")

    else:
        for i in range(numbers):
            stringlist.append(i)
            for s in strings(numbers, length, stringlist, depth+1):
                yield s
            stringlist.pop()

def fast_string_finder(numbers, length):


if __name__ == "__main__":
    import sys
    perfect_string_finder(int(sys.argv[1]), int(sys.argv[2]))