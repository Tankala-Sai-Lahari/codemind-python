s=list(input().lower())
c=[]
for i in s:
    if s.count(i)==1 and i!=" ":
        c.append(i)
print("".join(sorted(c)))