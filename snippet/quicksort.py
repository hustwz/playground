def partition(seq):
    pi, seq = seq[0], seq[1:] # Pick and remove the pivot
    lo = [x for x in seq if x <= pi] # All the small elements
    hi = [x for x in seq if x > pi] # All the large ones
    return lo, pi, hi # pi is "in the right place"
def quicksort(seq):
    if len(seq) <= 1: return seq # Base case
    lo, pi, hi = partition(seq) # pi is in its place
    return quicksort(lo) + [pi] + quicksort(hi) # Sort lo and hi separately

def quicksort2(seq):
    less = []
    equal = []
    greater = []
    if len(seq) <= 1:
        return seq
    for x in seq:
        if x < seq[0]:
            less.append(x)
        elif x == seq[0]:
            equal.append(x)
        else:
            greater.append(x)
    return quicksort2(less) + equal + quicksort2(greater)

def partition3(seq, low, high):
    key = seq[low]
    while low < high:
        while low < high and seq[high] > key:
            high -= 1
        if low < high:
            seq[low] = seq[high]
        while low < high and seq[low] <= key:
            low += 1
        if low < high:
            seq[high] = seq[low]
    seq[low] = key
    return low

def quicksort3(seq, low, high):
    if low < high:
        mid = partition3(seq, low, high)
        quicksort3(seq, low, mid-1)
        quicksort3(seq, mid+1, high)

def partition4(seq, low, high):
    i = low - 1
    j = low
    while j < high:
        if seq[j] <= seq[high]:
            i += 1
            seq[i], seq[j] = seq[j], seq[i]
        j += 1
    seq[i+1], seq[high] = seq[high], seq[i+1]
    return i+1

def quicksort4(seq, low, high):
    if low < high:
        mid = partition4(seq, low, high)
        quicksort4(seq, low, mid-1)
        quicksort4(seq, mid+1, high)
