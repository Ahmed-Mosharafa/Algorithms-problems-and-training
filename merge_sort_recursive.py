def merge(L1, L2):
    sort = []
    while (len(L1) != 0) and (len(L2) != 0):
        if L1[0] < L2 [0]:
            sort.append(L1.pop(0))
        else:
            sort.append(L2.pop(0))
    sort+= L1
    sort+= L2
    return sort 
def merge_sort(L):
    if len(L) < 2:
        return L
    left  = merge_sort(L[len(L)/2:])
    right = merge_sort(L[:len(L)/2])
    return merge(left, right)
        
print merge_sort(list)