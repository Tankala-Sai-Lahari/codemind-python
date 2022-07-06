s=input()
w=""
for i in s:
    if i not in w:
        w+=i
print(s==w)