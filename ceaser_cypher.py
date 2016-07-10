#!/bin/python

import sys,string

def check_boundaries(letter, k, list_ch):
    new_index = list_ch.index(letter) + k 
    boundary  = len(list_ch)
	new_index %= boundary
	#another solution
    #while (new_index >= boundary):
        #new_index -= boundary
    return list_ch[new_index]

n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())
upcase  = string.ascii_uppercase
lowcase = string.ascii_lowercase
ret = ""
for i in range(n):
    letter = s[i]
    if letter in upcase:
        letter = check_boundaries(letter, k, upcase)
    elif letter in lowcase:
        letter = check_boundaries(letter, k, lowcase)
    ret += letter
print ret