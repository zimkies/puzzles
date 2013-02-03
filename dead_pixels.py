import sys
import heapq
import numpy as np
from math import factorial

def solution(W, H, P, Q, N, X, Y, a, b, c, d):
    x = [X] * N
    y = [Y] * N
    for i in range(1, N):
        x[i] = (x[i-1] * a + y[i-1]*b +1) % W
        y[i] = (x[i-1] * c + y[i-1]*d +1) % H 
    deads = zip(x, y)

    #return dumbsol(W, P, H, Q, deads)
    return sol(W, P, H, Q, deads)
    #return fastsol(W, P, H, Q, deads)

def sol(W, P, H, Q, deads):
    matrix = np.zeros((W, H))
    c = 0
    for d in deads:
        c += 1
        print c
        matrix[max(0, d[0] - P + 1):d[0] + 1, max(0, d[1] - Q + 1):d[1] + 1] = 1
#        for i in range(max(0, d[0] - P+ 1), d[0] +1):
#            for j in range(max(0, d[1] - Q + 1), d[1] + 1):
#                matrix[i,j] = 1

    #print matrix
    count = 0

    for j in range(H-Q +1):
        for i in range(W-P+1):
            print i,j 
            if matrix[i,j] == 0:
                count += 1
        
    return count

def fastsol(W, P, H, Q, deads):
    matrix = np.zeros((W, H))
    deads.sort(key=lambda x: sorted(list(x), reverse=True))
    #print deads
    c = 0
    for x, y in deads:

        rangey = max(-1, y - Q)
        rangex = max(-1, x - P)
        done = False

        c += 1
        print c, y, rangey, x, rangex
        for j in range(y, rangey, -1):
            for i in range(x, rangex, -1):
                if matrix[i,j] == 1:
                    if i == x:
                        done = True
                    rangex = i
                    break 
                matrix[i,j] = 1

            if done:
                break

    #print matrix
    count = 0
    for i in range(W-P+1):
        for j in range(H-Q +1):
            if matrix[i,j] == 0:
                count += 1
        
    return count



def dumbsol(W, P, H, Q, deads):
    count = 0
    for i in range(W-P + 1):
        for j in range(H-Q + 1):
            found = False
            for k, dead in enumerate(deads):
                if i <= dead[0] < i + P and j <= dead[1] < j +  Q:
                    found = True
                    break 
            if not found:
                count += 1

    return count 


if __name__ ==  '__main__':
    filep = open(sys.argv[1])
    t  = int(filep.readline())
    for l in range(t):
    #for l in range(1):
        W, H, P, Q, N, X, Y, a, b, c, d = map(int, filep.readline().split())
        ans = solution(W, H, P, Q, N, X, Y, a, b, c, d)
        print 'Case #%d: %s' % (l+1, ans)
