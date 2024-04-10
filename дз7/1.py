def binary_search(data, needle):
    l = 0
    r = len(data)

    if r == 0 or needle < data[0] or needle > data[-1]:
        return -1
    
    while l <= r:
        mid = (l + r) // 2

        if needle == data[mid]:
            print ('true')
            return
        
        if needle < data[mid]:
            r = mid - 1
        else:
            l = mid + 1

    print('false')

arr_cnt = int(input())
arr = list(map(int, input().split()))
num = int(input())

binary_search(arr, num)