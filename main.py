import time

teste = open("teste.txt")
f = open("numbers.txt")
T = teste.readline().strip("T= ").strip()

def bubbleSort(v, N):
    for i in range(int(N)):
        f = 0
        for j in range(0, int(N) - i - 1):
            if int(v[j]) > int(v[j + 1]):
                aux = v[j]
                v[j] = v[j + 1]
                v[j + 1] = aux
                f = 1
        if f == 0:
            break

# ------------------------

def countSort(v, N, Max):
    sorted_v = [0 for i in range(N)]
    count = [0 for i in range(Max+1)]
    for i in v:
        count[int(i)] += 1
    for i in range(1,Max+1):
        count[i] += count[i - 1]
    for i in range(N):
        sorted_v[count[int(v[i])] - 1] = v[i]
        count[int(v[i])] -= 1
    for i in range(N):
        v[i] = sorted_v[i]

# ------------------------

def countSort_Radix(v, N, Max, digit):
    sorted_v = [0 for i in range(N)]
    count = [0 for i in range(Max + 1)]
    for i in v:
        count[int(i) / digit % 10] += 1
    for i in range(1, Max + 1):
        count[i] += count[i - 1]
    i = N - 1
    while i >= 0:
        sorted_v[count[int(v[i]) / digit % 10] - 1] = v[i]
        count[int(v[i]) / digit % 10] -= 1
        i -= 1
    for i in range(N):
        v[i] = sorted_v[i]
    return v

def radixSort(v, Max):
    digit = 1
    while Max < digit:
        countSort_Radix(v, N, Max, digit)
        digit *= 10

# ------------------------

def mergeSort(v):
    if len(v) > 1:
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

# ------------------------

def part(v, i, j):
    piv = int(v[j]) # varianta cu ultimul element drept pivot
    p_curent = i - 1
    for k in range(i,j):
        if int(v[k]) < piv:
            p_curent += 1
            aux = v[p_curent]
            v[p_curent] = v[k]
            v[k] = aux
    aux = v[p_curent + 1]
    v[p_curent +1] = v[j]
    v[j] = aux
    return (p_curent + 1)

def quickSort(v, i, j):
    if i < j:
        index = part(v, i, j)
        quickSort(v, i, index - 1)
        quickSort(v, index + 1, j)

# ------------------------

for test in range(int(T)):
    sir = teste.readline()
    i1 = 0
    OK = 0
    for l in sir:
        if OK == 0:
            if l not in "0123456789":
                i1 = i1 + 1
            else:
                OK = 1
    i2 = i1
    OK = 0
    for l in range(i1,len(sir)-1):
        if OK == 0:
            if sir[l] in "0123456789":
                i2 = i2 + 1
            else:
                OK = 1
    j1 = i2
    N = sir[i1:i2 + 1]
    OK = 0
    for l in range(i2,len(sir) - 1):
        if OK == 0:
            if sir[l] not in "0123456789":
                j1 = j1 + 1
            else:
                OK = 1
    j2 = j1
    OK = 0
    for l in range(j1,len(sir) - 1):
        if OK == 0:
            if sir[l] in "0123456789":
                j2 = j2 + 1
            else:
                OK = 1
    Max = sir[j1:j2 + 1].strip()
    print("N = ", N, "Max = ", Max)

    v = f.readline().split()

    start = time.time()
    bubbleSort(v, int(N))
    stop = time.time()
    print("Bubble sort time: ", stop - start)

    start = time.time()
    countSort(v, int(N), int(Max))
    stop = time.time()
    print("Count sort time: ", stop - start)

    start = time.time()
    radixSort(v, int(Max))
    stop = time.time()
    print("Radix sort time: ", stop - start)

    start = time.time()
    mergeSort(v)
    stop = time.time()
    print("Merge sort time: ", stop - start)

    start = time.time()
    quickSort(v, 0, int(N) - 1)
    stop = time.time()
    print("Quick sort time: ", stop - start, "\n")
