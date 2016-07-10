def insertion_sort(l):
    i = 1
    while i < len(l):
        j = i
        while (l[j-1] > l[j]) and j > 0:
            l[j], l[j-1] = l[j-1], l[j]
            j-=1
        i+=1
    return l