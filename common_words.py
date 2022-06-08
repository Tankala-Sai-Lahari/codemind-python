s1=input().lower().split()
s2=input().lower().split()
l=[]
for i in s1+s2:
    if i in s1 and i in s2 and i not in l:
        l.append(i)
for i in s2:
    if i in l:
        print(i,end=" ")