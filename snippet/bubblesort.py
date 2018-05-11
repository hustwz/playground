def bubbleSort(seq):
    for i in range(0, len(seq)-1):
        for j in range(0, len(seq)-1-i):
            if seq[j] > seq[j+1]:
                seq[j+1], seq[j] = seq[j], seq[j+1]
    return seq
