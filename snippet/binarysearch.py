def binarySearch(seq, key):
    i = 0
    j = len(seq) - 1
    while i <= j:
        mid = i + (j-i) / 2
        if key == seq[mid]:
            return mid
        elif key < seq[mid]:
            j = mid - 1
        else:
            i = mid + 1
    return -1
