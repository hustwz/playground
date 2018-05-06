def merge(l, r):
    i = j = 0
    res = []
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    res += l[i:]
    res += r[j:]
    return res

def mergesort_using_recursion(seq):
    if len(seq) <= 1:
        return seq
    mid = len(seq)/2
    l, r = seq[:mid], seq[mid:]
    l = mergesort_using_recursion(l)
    r = mergesort_using_recursion(r)
    return merge(l, r)
