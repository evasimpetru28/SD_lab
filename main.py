teste = open("teste.txt")
f = open("numbers.txt")
T = teste.readline().strip("T= ").strip()

def bubbleSort(v, N):
    for i in range(0,N-1):
        for j in range(0, N-i-1):
            if v[j] > v[j+1]:
                aux = v[j]
                v[j] = v[i]
                v[i] = aux

def countSort(v, N, Max):
    sorted_v = [0 for i in range(N)]
    count = [0 for i in range(Max+1)]
    for i in v:
        count[int(i)] += 1
    for i in range(1,Max+1):
        count[i] += count[i-1]
    for i in range(N):
        sorted_v[count[int(v[i])]-1] = v[i]
        count[int(v[i])] -= 1
    for i in range(N):
        v[i] = sorted_v[i]
    return v

def countSort_Radix(v, N, Max, digit):
    sorted_v = [0 for i in range(N)]
    count = [0 for i in range(Max + 1)]
    for i in v:
        count[int(i)/digit%10] += 1
    for i in range(1, Max + 1):
        count[i] += count[i - 1]
    i = N-1
    while i >= 0:
        sorted_v[count[int(v[i])/digit%10] - 1] = v[i]
        count[int(v[i])/digit%10] -= 1
        i -= 1
    for i in range(N):
        v[i] = sorted_v[i]
    return v

def radixSort(v, Max):
    digit = 1
    while Max < digit:
        countSort_Radix(v, N, Max, digit)
        digit *= 10
    return v

for test in range(ord(T)-48):
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
    N = sir[i1:i2+1]
    OK = 0
    for l in range(i2,len(sir)-1):
        if OK == 0:
            if sir[l] not in "0123456789":
                j1 = j1 + 1
            else:
                OK = 1
    j2 = j1
    OK = 0
    for l in range(j1,len(sir)-1):
        if OK == 0:
            if sir[l] in "0123456789":
                j2 = j2 + 1
            else:
                OK = 1
    Max = sir[j1:j2+1].strip()
    print("N = ", N, "Max = ", Max)

    v = f.readline().split()
    print(countSort(v, int(N), int(Max)))
    print(radixSort(v, int(Max)))