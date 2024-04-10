from math import ceil

def more_than_half(str):
    if len(str) == 2:
        print('-1')
        return 
    
    num = ceil(len(str) / 2)

    char_count = {}

    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for key, value in char_count.items():
        if value >= num:
            print(key)
            return
        
    print('-1')

string_cnt = int(input())
string = input().replace(' ', '')
more_than_half(string)