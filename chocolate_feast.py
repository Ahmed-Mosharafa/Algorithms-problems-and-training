#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    num_of_choc = n/c
    wrappers = num_of_choc
    while (wrappers/m != 0):
        #new bonus
        bonus = wrappers/m 
        #remaining wrappers are the one of bonus, wrappers%m(remaining wrappers)
        wrappers = bonus + wrappers%m
        #adding bonus to no of chocs
        num_of_choc += bonus
    print num_of_choc