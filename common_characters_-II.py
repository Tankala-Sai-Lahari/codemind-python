s1=input().lower()
s2=input().lower()
l=[]
for i in s1:
    if i in s2 and i not in l and i!=" ":
        l.append(i)
print(len(l))
        