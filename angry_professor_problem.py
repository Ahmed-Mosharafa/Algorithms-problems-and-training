#!/bin/python

import sys
#A Discrete Mathematics professor has a class of  students. Frustrated with their lack of discipline, he decides to cancel class if #fewer than  students are present when class starts.
#Given the arrival time of each student, determine if the class is canceled.


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    a.sort()
    i = 0
    students = 0
    while a[i] <= 0:
        i+=1
    if i < k:
        print "YES"
    else:
        print "NO"