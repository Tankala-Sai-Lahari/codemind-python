s=input().lower()
l=[]
for i in s:
    if i not in l and i!=" ":
        l.append(i)
l.sort()
print("".join(l))