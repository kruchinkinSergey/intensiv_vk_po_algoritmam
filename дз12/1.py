def max_product_subsequence(sequence, k):
    max_product = float('-inf')
    for i in range(len(sequence) - k + 1):
        product = 1
        for j in range(i, i + k):
            product *= sequence[j]
        max_product = max(max_product, product)
    return max_product


arr_cnt = int(input())
arr = list(map(int, input().split()))
k =  int(input())
result = max_product_subsequence(arr, k)
print(result)