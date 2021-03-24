def breach(seq, v, l, r):
    # search for v in seq[l:r]

    if r - l == 0:
        return False
    mid = (r - l) // 2
    if v == seq[mid]:
        return mid

    if v < seq[mid]:
        return breach(seq, v, l, mid)
    if v > seq[mid]:
        return breach(seq, v, mid + 1, r)


s = [1, 23, 29, 34, 41, 50, 62, 69, 71, 76]
l = 0
r = len(s)
v = 76
print("Index of number is")
print(breach(s, v, l, r))
