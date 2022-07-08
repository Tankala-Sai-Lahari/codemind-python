n,s=map(int,input().split())
n=str(n)
n1=int(n[0:s])
n2=int(n)%10**s
print(abs(n2-n1))