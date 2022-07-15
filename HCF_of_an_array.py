def solve(num):
    def gcd(a,b):
        if b==0:
            return a
        else:
            return gcd(b,a%b)
    if len(num)==1:
        return num[0]
    div=gcd(num[0],num[1])
    if len(num)==2:
        return div
    for i in range(1,len(num)-1):
        div=gcd(div,num[i+1])
        if div==1:
            return div
    return div
n=int(input())
l=list(map(int,input().split()))
print(solve(l))