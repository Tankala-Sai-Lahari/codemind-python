l=input().split()
c=0
for i in l:
    i=i.lower()
    if i==i[::-1]:
        c+=1
print(c)