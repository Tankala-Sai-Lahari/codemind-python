s=list(input().lower())
l=[]
for i in s:
    if i not in l and i!=" " and s.count(i)<=1:
        l.append(i)
print(len(l))
