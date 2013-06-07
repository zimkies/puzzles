#!/usr/bin/python

""" smallworld """
import sys
import random

    #* 1 <= P <= 1000
    #* 1 <= T <= 1000
    #* 1 <= Z <= 1000
    #* 1 <= s <= 100000
    #* 1 <= m <= 5000

P = 1000
T = 20#1000
Z = 1000
S = 335#100000
M = 5000


planets = 1000
print planets
for p in range(planets):
    zergs = 1000
    tbases = p+1
    print tbases, zergs
    for t in range(tbases):
        s = random.randint(1, S)
        m = random.randint(1,M)
        print s, m
#planets = random.randint(1,P)
#print planets
#for p in range(planets):
#    zergs = random.randint(1,Z)
#    tbases = random.randint(1,T)
#    print tbases, zergs
#    for t in range(tbases):
#        s = random.randint(1, S)
#        m = random.randint(1, M)
#        print s, m
    