s=input()
f=[]
for i in s:
    if i in "aeiouAEIOU" and i not in f:
        f.append(i)
if len(f)>0:
    print(*f)
else:
    print(-1)