import sys
import heapq
from math import factorial

class Solution:

    def __init__(self, m, k1, k2):
        self.m = m
        self.k1 = k1.strip()
        self.k2 = k2.strip()
        self.n = len(self.k1)
        self.seg = int(self.n / m)

    def solution(self):
        
        # Setup
        k1s = []
        k2s = []
        k2ss = {}

        for i in range(self.m):
            k1s.append(self.k1[i*self.seg:(1+i)*(self.seg )])
            k2s.append(self.k2[i*self.seg:(1+i)*(self.seg )])
            k2ss[k2s[i]] = k2ss.get(k2s[i], 0) + 1

        ck1s = k1s[:]

        ck1s.sort()

        solved, t = solver(k1s, k2ss, 0, self.m, self.seg)
        if solved:
            return "".join(solved)
        else:
            return "IMPOSSIBLE"

def solver(k1s, k2ss, i, length, seg):
    if i == length:
        return [], True
    for k2, v2 in k2ss.items():
        sim, t = similar(k1s[i], k2, 0, seg)
        if sim:
            if not v2:
                del k2ss[k2]
            else:
                k2ss[k2] -= 1
            sol, t = solver(k1s, k2ss, i+1, length, seg)
            if t:
                return [sim] + sol, t 
            k2ss[k2] = k2ss.get(k2, 0) + 1

    return [], False
    

def picker(c1, c2):
    if c1 == '?':
        if c2 == '?':
            return 'a'
        return c2
    if c2 == '?':
        return c1
    if c1 == c2:
        return c1
    return None

def similar(k1, k2, i, length):
    ''' Return similarity of k1 and k2 or "" if not'''
    if i == length:
        return "", True
    if length == 0:
        return "", False

    c = picker(k1[i], k2[i])
    if c:
        val, t = similar(k1, k2, i+1, length)
        if t:
            return c + val, t

    return "", False

if __name__ ==  '__main__':
    filep = open(sys.argv[1])
    t  = int(filep.readline())
    for l in range(t):
        m = map(int, filep.readline().split())[0]
        k1 = filep.readline()
        k2 = filep.readline()
        ans = Solution(m, k1, k2).solution()
        print 'Case #%d: %s' % (l+1, ans)
