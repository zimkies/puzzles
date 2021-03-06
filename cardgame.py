'''
CARD GAME (20 points)

John is playing a game with his friends. The game’s rules are as follows: There is deck of N cards from which each person is dealt a hand of K cards. Each card has an integer value representing its strength. A hand’s strength is determined by the value of the highest card in the hand. The person with the strongest hand wins the round. Bets are placed before each player reveals the strength of their hand.

John needs your help to decide when to bet. He decides he wants to bet when the strength of his hand is higher than the average hand strength. Hence John wants to calculate the average strength of ALL possible sets of hands. John is very good at division, but he needs your help in calculating the sum of the strengths of all possible hands.

PROBLEM

You are given an array a with N ≤ 10000 different integer numbers and a number, K, where 1 ≤ K ≤ N. For all possible subsets of a of size K find the sum of their maximal elements modulo 1000000007.

INPUT

The first line contains the number of test cases T, where 1 ≤ T ≤ 25

Each case begins with a line containing integers N and K. The next line contains N space-separated numbers 0 ≤ a [i] ≤ 2000000000, which describe the array a.

OUTPUT

For test case i, numbered from 1 to T, output "Case #i: ", followed by a single integer, the sum of maximal elements for all subsets of size K modulo 1000000007.

EXAMPLE

For a = [3, 6, 2, 8] and N = 4 and K = 3, the maximal numbers among all triples are 6, 8, 8, 8 and the sum is 30.

EXAMPLE INPUT

    5
    4 3
    3 6 2 8
    5 2
    10 20 30 40 50
    6 4
    0 1 2 3 5 8
    2 2
    1069 1122
    10 5
    10386 10257 10432 10087 10381 10035 10167 10206 10347 10088

EXAMPLE OUTPUT

    Case #1: 30
    Case #2: 400
    Case #3: 103
    Case #4: 1122
    Case #5: 2621483
'''
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
