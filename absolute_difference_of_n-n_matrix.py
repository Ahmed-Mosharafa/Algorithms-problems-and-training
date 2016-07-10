
import sys

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
#next diagonal is n+1
diag1_sum = 0
diag2_sum = 0
x = 0
y = n-1
for i in a:
    diag1_sum += i[x]
    diag2_sum += i[y]
    x+=1
    y-=1
print abs(diag1_sum-diag2_sum)