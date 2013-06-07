import sys

def valid_sentence(string):
    tracker = [0]
    for i, s in enumerate(string[:]):
        if s == '(':
            tracker = [t+1 for t in tracker] 
            if i and string[i-1] == ":":
                tracker.extend([t-1 for t in tracker])

        elif s == ')':
            tracker = [t-1 for t in tracker]
            if i and string[i-1] == ":":
                tracker.extend([t+1 for t in tracker])
        tracker = filter(lambda t: t >= 0, tracker)
        if not len(tracker):
            return False
    if 0 in tracker:
        return True
    return False


if __name__ ==  '__main__':
    filep = open(sys.argv[1])
    m  = int(filep.readline())
    for i, line in enumerate(filep):
        string = line
        truth = valid_sentence(string)
        if truth:
            t = "YES" 
        else:
            t = "NO" 

        print 'Case #%d: %s' % (i+1, t)
