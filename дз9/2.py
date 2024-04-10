def max_repeats(input_str):
    char_count = {}
    
    for char in input_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    max_repeat = max(char_count.values())
    
    return max_repeat

input_str = input()
result = max_repeats(input_str)
print(result)