import sys
import heapq
from math import factorial

MOD = 1000000007

class Total:

    def __init__(self, nums, n, k):
        self.nums = nums
        self.n = n
        self.k = k

        # Sort
        self.nums.sort()
        self.memo = {}
        self.fmemo = {}
    
    def total(self):
        total = 0
        for i in range(self.k-1, self.n):
            total = (total +  nums[i] * self.nchoosek(i, k-1)) % MOD
        return total 

    def nchoosek(self, n, k):
        if self.memo.get((n,k)):
            return self.memo.get((n,k))
        else:
            nk = int(self.fact(n) / (self.fact(n-k) * self.fact(k)))
            self.memo[(n,k)] = nk % MOD
            return nk

    def fact(self, k):
        if self.fmemo.get(k):
            return self.fmemo.get(k)
        else:
            if self.fmemo.get(k-1):
                nk = self.fmemo.get(k-1) * k
            else:
                nk = factorial(k) 
            self.fmemo[k] = nk

            return nk
  
if __name__ ==  '__main__':
    filep = open(sys.argv[1])
    t  = int(filep.readline())
    for l in range(t):
        n, k = map(int, filep.readline().split())
        nums = map(int, filep.readline().split())
        ans = Total(nums, n, k).total()
        print 'Case #%d: %s' % (l+1, ans)
