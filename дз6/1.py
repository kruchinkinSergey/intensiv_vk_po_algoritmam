string = input()
new_string = ''

def gg(str, new_str):
    isPrevPop = False
    isPrevIn = False
    for i in range(1, len(str)-1):
        prev = i-1
        cur = i
        next = i+1
        if str[cur] == str[prev]:
           isPrevPop = True
           continue
        else:
            if isPrevPop == False and isPrevIn == False:
                new_str += string[prev]

            if str[cur] == str[next]:
                continue
            else:
                new_str += string[cur]
                isPrevIn = True
    
    if str[-1] != str[-2]:
        new_str += str[-1]

    str = new_str
    return str
try:
    for i in range(3):
        string = gg(string, new_string)
except IndexError:
    for i in range(2):
        string = gg(string, new_string)
        
print(string)
