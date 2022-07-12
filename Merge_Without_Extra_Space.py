t=int(input())
for z in range(t):
    a,b=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    print(*sorted(l1+l2))