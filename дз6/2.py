arrCnt = int(input())
array = list(map(int, input().split()))
even_number = []

try:
    for i in range(arrCnt-1, -1, -1):
        if array[i] % 2 == 0:
            even_number.append(array[i])
            break

    if even_number:
        print(even_number[-1])
    else:
        print('-1')   
except EOFError: 
    pass        
