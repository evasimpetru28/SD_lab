f=open("teste.txt")


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


v = f.readline().split()
print(v)

countSort(v, len(v), 99)
print("Vectorul printat: ",v)

