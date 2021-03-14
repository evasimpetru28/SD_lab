f = open("numbers.txt")


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if int(L[i]) < int(R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

v = f.readline().split()
print(mergeSort(v))

m = len(v) // 2
    st = v[:m]
    dr = v[m:]
    mergeSort(st)
    mergeSort(dr)
    i = j = k = 0
    while i < len(st) and j < len(dr):
        if int(st[i]) <= int(dr[j]):
            v[k] = st[i]
            i += 1
        else:
            v[k] = dr[j]
            j += 1
        k += 1
    while i < len(st):
        v[k] = st[i]
        i += 1
        k += 1
    while j < len(dr):
        v[k] = dr[j]
        j += 1
        k += 1
    return v