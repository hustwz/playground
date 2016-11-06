def mergesort(seq):
    mid = len(seq)//2 # Midpoint for division
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1: lft = mergesort(lft) # Sort by halves
    if len(rgt) > 1: rgt = mergesort(rgt)
    res = []
    while lft and rgt: # Neither half is empty
        if lft[-1] >= rgt[-1]: # lft has greatest last value
            res.append(lft.pop()) # Append it
        else: # rgt has greatest last value
            res.append(rgt.pop()) # Append it
    res.reverse() # Result is backward
    return (lft or rgt) + res # Also add the remainder
