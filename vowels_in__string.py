s=input()
l=[]
for i in s:
    if i in "AEIOUaeiou" and i not in l:
        l.append(i)
print(*l)