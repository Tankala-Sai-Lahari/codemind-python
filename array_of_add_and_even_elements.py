n=int(input())
l=list(map(int,input().split()))
o,e=[],[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print(*(o+e))