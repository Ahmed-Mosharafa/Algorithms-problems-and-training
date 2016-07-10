#!/bin/python

import sys

#You are given an array of  integers, , and a positive integer, . Find and print the number of pairs where  and  +  is evenly divisible #by .

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))

a.sort()
counter = 0
for i in range(n-1):
    for j in range(i+1, n):
        if ((a[i] + a[j]) % k ) == 0:
            counter +=1 
print counter