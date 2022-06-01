n,m=map(int,input().split())
l=[]
for i in range(n):
    t=list(map(int,input().split()))
    l.append(t)
c=0
for i in l:
    if i==sorted(i) or i[::-1]==sorted(i):
        c+=1
print(c)