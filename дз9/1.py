def is_anagram(str, str2):
    if len(str) != len(str2):
        print('false')
        return

    char_count = {}
    char_count2 = {}

    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in str2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1

    if (char_count == char_count2):
        print('true')
    else:
        print('false')

string1, string2 = input().split(' ')
is_anagram(string1, string2)