arrCnt = input()
arr = list(map(int, input().split()))
element = int(input())

cnt = 0

for num in arr: 
    if num != element:
        cnt += 1

print(cnt)