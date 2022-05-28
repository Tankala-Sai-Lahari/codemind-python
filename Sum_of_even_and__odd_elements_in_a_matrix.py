n,m=map(int,input().split())
l=[]
e,o=0,0
for i in range(n):
    l.extend(list(map(int,input().split())))
for i in l:
    if i%2==0:
        e+=i
    else:
        o+=i
print(e,o)