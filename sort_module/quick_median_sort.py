def mot(D, e, f):
    mid = (e + f - 1) // 2
    a = D[e]
    b = D[mid]
    c = D[f - 1]
    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, e - 1
    if b <= c <= a:
        return c, f - 1
    return a, e

def qsm(L, s, e, asc=True):
    result = 0
    if s < e:
        pivot_location, result = Partition(L, s, e, asc)
        result += qsm(L, s, pivot_location, asc)
        result += qsm(L, pivot_location + 1, e, asc)
    return result

def Partition(L, s, e, asc=True):
    result = 0
    pivot, pida = mot(L, s, e)
    L[s], L[pida] = L[pida], L[s]
    i = s + 1
    for j in range(s + 1, e, 1):
        result += 1
        if (asc and L[j] < pivot) or (not asc and L[j] > pivot):
            L[i], L[j] = L[j], L[i]
            i += 1
    L[s], L[i - 1] = L[i - 1], L[s]
    return i - 1, result

def quicksortmedian(l, asc=True):
    qsm(l, 0, len(l), asc)