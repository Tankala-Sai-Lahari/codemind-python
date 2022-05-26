s=input()
l=[]
d=[]
for i in s:
    if i in "AEIOUaeiou" and i not in l:
        l.append(i)
for i in "aeiou":
    if i not in l:
      d.append(i)  
d.sort()
if len(d)>0:
    print(*d)
else:
    print(0)