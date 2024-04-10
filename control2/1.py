def exponential_search(data, needle):
    border = 1
    lastElement = len(data)-1
    while border < lastElement and data[border] < needle:
        border = border * 2
        if data [border] == needle:
            return border
        
        if border > lastElement:
            border = lastElement
    print(border//2, border)  

arr_cnt = int(input())
arr = list(map(int, input().split()))
required_el = int(input())

exponential_search(arr, required_el)