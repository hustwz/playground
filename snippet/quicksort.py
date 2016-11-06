def partition(seq):
    pi, seq = seq[0], seq[1:] # Pick and remove the pivot
    lo = [x for x in seq if x <= pi] # All the small elements
    hi = [x for x in seq if x > pi] # All the large ones
    return lo, pi, hi # pi is "in the right place"
def quicksort(seq):
    if len(seq) <= 1: return seq # Base case
    lo, pi, hi = partition(seq) # pi is in its place
    return quicksort(lo) + [pi] + quicksort(hi) # Sort lo and hi separately
