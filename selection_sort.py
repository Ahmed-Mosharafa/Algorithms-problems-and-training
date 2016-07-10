def selection_sort(l):
    for i in range(1,len(l)):
        minimum = l.index(min(l[i:]))
        for j in range(i):
            if l[minimum] < l[j]:
                l[j], l[minimum] = l[minimum], l[j]
    return l