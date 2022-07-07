s=input().lower()
t=""
for i in s:
    if i.isalpha() and i not in t:
        t+=i
print(len(t)==26)
    