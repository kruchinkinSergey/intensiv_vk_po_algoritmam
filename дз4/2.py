# books_cnt = int(input())
# arr = []

# for i in range(books_cnt):
#     arr.append(input().split())

# arr_years = []

# for i in range(len(arr)):
#     arr_years.append(arr[i][2])

# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i = j = k = 0
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1    

# merge_sort(arr_years)

# sorted_arr = []

# for item in arr_years:
#     for i in range(len(arr)):
#         if (str(item) in arr[i]):
#             sorted_arr.append(arr.pop(i))


# print(' '.join(map(str, sorted_arr)))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][2] == right[j][2]:
            if left[i][1] < right[j][1]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif left[i][2] < right[j][2]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Ввод данных
books = []
n = int(input())
for _ in range(n):
    books.append(input().split())

# Сортируем книги
sorted_books = merge_sort(books)

# Выводим отсортированные книги
for book in sorted_books:
    print(f"{book[0]} \"{book[1]}\" {book[2]}")