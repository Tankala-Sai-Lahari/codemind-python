l=input().split()
l1=[]
for i in l:
    c=0
    for j in i:
        if j in "aeiouAEIOU":
            c+=1
    l1.append(c)
print(l1.count(min(l1)))