def freq_sort(l):
    d = {}
    for i in l:
        d[i] = l.count(i)
    x = collections.OrderedDict(sorted(d.items() ,key = lambda x: x[1] , reverse = True))
    return x.keys()