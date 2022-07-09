n=int(input())
l=list(map(int,input().split()))
l=sorted(set(l))
if n>=3:
    print(l[-3])
else:
    print(l[n-1])