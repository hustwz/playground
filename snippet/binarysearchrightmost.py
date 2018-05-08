def binarysearchrightmost(seq, key):
    i = 0
    j = len(seq) - 1
    while i < j:
        m = i + ((j + 1 - i) >> 1)
        if key < seq[m]:
            j = m - 1
        else:
            i = m
    if seq[i] == key:
        return i
    else:
        return -1
