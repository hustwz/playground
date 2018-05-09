def bubbleSort(seq):
    for i in range(0, len(seq)-1):
        for j in range(i+1, len(seq)):
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
    return seq
