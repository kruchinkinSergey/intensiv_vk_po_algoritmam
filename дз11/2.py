def find_min_product(arr):
    if not arr:
        return None

    index_min = 0

    while 2 * index_min + 1 < len(arr):
        index_min = 2 * index_min + 1

    return arr[index_min] 

arr_cnt = int(input())
arr = list(map(int, input().split()))
print(find_min_product(arr))