s = input("Enter string: ")
result = ""

for ch in s:
    found = False

    for r in result:
        if ch == r:
            found = True
            break

    if not found:
        result += ch

print(result)