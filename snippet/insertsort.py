def insert_sort(seq):
    if len(seq) <= 1:
        return seq
    i = 1
    while i <= len(seq) - 1:
        j = i
        while j > 0 and seq[j] < seq[j-1]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
        i += 1
    return seq
