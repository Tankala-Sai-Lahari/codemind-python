n=int(input())
l=list(map(int,input().split()))
x=int(input())
m=max(l)
t=[]
for i in l:
    if i+x>=m:
        t.append(True)
    else:
        t.append(False)
print(*t)