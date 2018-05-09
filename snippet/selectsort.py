def selectsort(seq):
    for i in range(0, len(seq)-1):
        min = i
        for j in range(i+1, len(seq)):
            if seq[j] < seq[min]:
                min = j
        seq[min], seq[i] = seq[i], seq[min]
    return seq
