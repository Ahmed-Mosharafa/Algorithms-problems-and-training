#!/bin/python

#There are two kangaroos on an x-axis ready to jump in the positive direction (i.e, toward positive infinity). The first kangaroo #starts at location  and moves at a rate of  meters per jump. The second kangaroo starts at location  and moves at a rate of  meters #per jump. Given the starting locations and movement rates for each kangaroo, can you determine if they'll ever land at the same #location at the same time?

import sys


x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

if v2 != v1:
    test = (x1-x2) % (v2-v1)
    sign_test = (x1-x2) / (v2-v1)
    if (test == 0) and (sign_test >= 0):
        print "YES"
    else:
        print "NO"
else:
    print "NO"