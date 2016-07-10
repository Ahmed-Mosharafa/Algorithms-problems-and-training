import math
x = int(raw_input())
y = int(raw_input())
answer = ""
for i in xrange(x,y+1):
    ind = "1"
    squared = i**2
    ind += "0" * int(math.ceil(len(str(squared))/2.0))
    if (squared%int(ind) + squared/int(ind)) == i:
        answer += str(i) + " "
if answer != "":
    print answer.strip() 
else:
    print "INVALID RANGE"