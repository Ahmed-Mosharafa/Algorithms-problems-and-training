#strings, grade school algorithm
x,y = 1222,122
ind = ""
add_l = []
for i in str(y).strip()[::-1]:
    partial = ""
    rem = "0"
    for n in str(x).strip()[::-1]:
        mult = str(int(i) * int(n) + int(rem))
        rem  = mult [:-1] if mult[:-1] != "" else "0"
        partial = mult[-1] + partial 
    add_l.append(partial + ind)
    ind += "0"
    print reduce(lambda x,y: int(x)+int(y), add_l)

#Karatsuba Multiplication
#x,y = 5678,1234
#divide number into two halves
#x.y = 10^n ac + 10^n/2 (ad+bc) +bd
def karatsuba(x,y):
    if(x<10) or (y<10):
        return x*y
    else:
        stringx, stringy = str(x), str(y)
        a,b = int(stringx[:len(stringx)/2]),int(stringx[len(stringx)/2:])
        c,d = int(stringy[:len(stringy)/2]),int(stringy[len(stringy)/2:])
        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        adbc = karatsuba(a+b, c+d) - (ac+bd)
        length =len(str(x))
        return (10**length *ac) + (10**(length/2) * adbc) + bd 
print karatsuba(12, 13)

import math 
def karatsuba_mod(x,y):
    if(x<10) or (y<10):
        return x*y 
    else:
        length = int(math.log10(x)) + 1 
        