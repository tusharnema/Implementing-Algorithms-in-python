def in_trav(a, t, i, n):
    if i < n:
        in_trav(a, t, 2 * i + 1, n)
        
