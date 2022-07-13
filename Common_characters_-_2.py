l=input().lower().split()
c=0
for i in l[0]:
    for j in l:
        if i not in j:
            break
    else:
        c+=1
print(c)