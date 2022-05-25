n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    k.append(int(str(i)[::-1]))
print(*k)