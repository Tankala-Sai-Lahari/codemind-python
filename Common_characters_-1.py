l=input().lower().split()
c=""
for i in l[0]:
    for j in l:
        if i not in j:
            break
    else:
        c+=i
if c=="":
    print(-1)
else:
    print(c)