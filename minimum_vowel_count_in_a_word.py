l=input().split()
l1=[]
for i in l:
    c=0
    for j in i:
        if j in "AEIOUaeiou":
            c+=1
    l1.append(c)
print(min(l1))