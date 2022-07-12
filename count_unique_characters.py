l=list(input().lower())
t=[]
for i in l:
    if i not in t and l.count(i)==1 and i!=" ":
        t.append(i)
print(len(t))
