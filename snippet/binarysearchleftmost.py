def binarySearchleftmost(seq, key):
    i = 0
    j = len(seq) - 1
    while i < j:
        mid = i + (j-i) / 2
        if key <= seq[mid]:
            j = mid
        else:
            i = mid + 1
    return i
