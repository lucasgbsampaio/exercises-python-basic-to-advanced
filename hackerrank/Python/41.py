string_s = input()
length = int(input())

s_list = []
for i in range(0, len(string_s), length):
    split = string_s[i:i+3]
    string = ''
    for j in split:
        if j not in string:
            string += j
    s_list.append(string)

print(*s_list, sep='\n')