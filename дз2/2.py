# arrCnt = int(input())
# arr = list(map(int, input().split()))

# for i in range(arrCnt): 
#     if arr[i] == 0:
#         arr.append(arr.pop(i))
        

# print(arr)

arrCnt = int(input())
arr = list(map(int, input().split()))

new_arr = []

for i in range(arrCnt):
    if arr[i] != 0:
        new_arr.append(arr[i])

for i in range(arrCnt):
    if arr[i] == 0:
        new_arr.append(0)

print(' '.join(map(str, new_arr)))
