arrCnt = int(input())
arr = list(map(int, input().split()))
index = 0

for i in range(arrCnt):
    if (arr[i] % 2 == 0):
        arr[i], arr[index] = arr[index], arr[i]
        index += 1

print(' '.join(map(str, arr)))