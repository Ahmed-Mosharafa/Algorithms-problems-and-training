#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    num_of_choc = n/c
    wrappers = num_of_choc
    while (wrappers >= m):
        wrappers -= m-1
        num_of_choc += 1
    print num_of_choc