s=input().split()
for i in s:
    c=0
    for j in i:
        if j in "AEIOUaeioiu":
            c+=1
    print(c,end=" ")