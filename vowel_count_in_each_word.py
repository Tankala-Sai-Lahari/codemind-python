l=input().split()
s=[]
for i in l:
    c=0
    for j in i:
        if j in "AEIOUaeiou" :
            c+=1
    s.append(c)
print(*s)