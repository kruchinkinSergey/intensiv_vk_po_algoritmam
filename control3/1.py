def find_max_product(arr):
    if not arr:
        return None

    index_max = 0

    while 2 * index_max + 2 < len(arr):
        index_max = 2 * index_max + 2

    return arr[index_max] 

arr_cnt = int(input())
arr = list(map(int, input().split()))
print(find_max_product(arr))