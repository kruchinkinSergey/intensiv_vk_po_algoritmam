def interpolation_search(data, needle):
    left = 0
    right = len(data) - 1
    # выполняем наш поиск, пока заданное число находится в границах
    # массива,
    # точнее, пока граница не сведётся к нулю
    while data[left] < needle < data[right]:
        if data[left] == data[right]:
            break
        index = left + (right - left) * (needle - data[left]) // (data[right] - data[left])
        # в зависимости от того, больше ли искомое число или меньше,
        # сдвигаем соответствующим образом наши границы
        if data[index] > needle:
            right = index - 1
            # print('right: ', right)
        elif data[index] < needle:
            left = index + 1
            # print('left: ', left)
        else:
            print(index)
            return
        # после выхода из цикла остаётся проверить значения границ
        if data[left] == needle:
            return left
        if data[right] == needle:
            return right
        # если не нашли, то возвращаем минус единицу
        print(left)
        return
    
arr_cnt = int(input())
arr = list(map(int, input().split()))
num = int(input())

interpolation_search(arr, num)