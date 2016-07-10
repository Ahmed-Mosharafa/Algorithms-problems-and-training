# Enter your code here. Read input from STDIN. Print output to STDOUT
def paranthesis(x):
    list1 = []
    dic= {"circular" : "()", "squared" : "[]", "curly" : "{}"}
    for i in x:
        if i in map(lambda x: x[0], dic.values()):
            list1.append(i)
        else:
            if i in map(lambda x: x[1], dic.values()):
                if len(list1)!=0:
                    if list1[-1]+i in dic.values():
                        list1.pop()
                    else:
                        return "NO"
                else:
                    return "NO"
    if len(list1) != 0:
        return "NO"
    else:
        return "YES"
number = int(raw_input(""))
paran  = []
for i in xrange(number):
    paran.append(raw_input(""))
for i in paran:
    print paranthesis(i)