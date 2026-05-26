s = input("Enter string: ")

longest = ""

for i in range(len(s)):
    temp = ""
    for j in range(i, len(s)):
        if s[j] not in temp:
            temp += s[j]
        else:
            break

    if len(temp) > len(longest):
        longest = temp

print(longest)