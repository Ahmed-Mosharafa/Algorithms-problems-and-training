#!/bin/python
#You are given N sticks, where the length of each stick is a positive integer. A cut operation is performed on the sticks such that all of them are reduced by the length of the smallest stick. this is done through subtracting the value of the smallest string from the whole strings
import sys

def divide(arr,):
    return x/y

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
while (len(arr) != 0):
    print len(arr)
    minim = min(arr)
    arr = map(lambda x: x-x if x < minim else x- minim, arr)
    arr = filter(lambda x: x!= 0, arr)