def in_trav(a, t, i, n):
    if i < n:
        in_trav(a, t, 2 * i + 1, n)
        t.append(a[i])
        in_trav(a, t, 2 * i + 2, n)
