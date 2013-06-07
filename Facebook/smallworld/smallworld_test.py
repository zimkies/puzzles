#!/usr/bin/python

""" smallworld """
import sys
import numpy
import random


def testgenerator(n):
    for i in range(1, n+1):
        print i, 180*(random.random()-.5), 360*(random.random()-.5)
        
testgenerator(100000)
