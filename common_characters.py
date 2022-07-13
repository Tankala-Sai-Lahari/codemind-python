s1=input().lower()
s2=input().lower()
l=[]
for i in s1+s2:
    if i in s1 and i in s2 and i!=" " and i not in l:
        l.append(i)
if l==[]:
    print(-1)
else:
    print("".join(sorted(l)))