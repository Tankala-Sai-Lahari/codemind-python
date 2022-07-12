n=int(input())
l=list(map(int,input().split()))
t=[]
p=l[n//2:n]
t.extend(p[::-1])
p=l[:n//2]
t.extend(p)
print(*t)