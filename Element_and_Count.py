n=int(input())
l=list(map(int,input().split()))
t=[]
for i in l:
    if i not in t:
        t.append(i)
for i in t:
    print(i,l.count(i),end=" ")