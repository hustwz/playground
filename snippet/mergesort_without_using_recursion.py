def merge(seq, low, mid, high):
    i = low
    j = mid
    res = []
    while i < mid and j < high:
        if seq[i] <= seq[j]:
            res.append(seq[i])
            i += 1
        else:
            res.append(seq[j])
            j += 1
    res += seq[i:mid]
    res += seq[j:high]
    seq[low:high] = res

def mergesort_without_using_recursion(seq):
    i = 1
    while i < len(seq):
        low = 0
        while low < len(seq):
            mid = low + i
            high = min(low + 2 * i, len(seq))
            if mid < high:
                merge(seq, low, mid, high)
            low += 2 * i
        i *= 2
    return seq
