t=int(input())
for z in range(t):
    n,k=map(int,input().split())
    s=input()
    for i in range(k,0,-1):
        s=s[:i][::-1]+s[i:]
    print(s)