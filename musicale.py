s = list(input())

i = 0
while (i < len(s) - 1):
    if s[i] == s[i+1]:
        del s[i + 1]
        del s[i]
        i = 0
    else:
        i=i+1

print("".join(s))