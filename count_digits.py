n=int(input())
l=list(map(int,input().split()))
f=[]
for i in l:
    if i>0:
        f.append(len(str(i)))
    else:
        f.append(len(str(-1*i)))
print(*f)