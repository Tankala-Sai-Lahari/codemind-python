def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def lcm(a,b):
    return (a*b//gcd(a,b))
n=int(input())
l=list(map(int,input().split()))
l.sort()
lcmm=lcm(l[0],l[1])
for i in l[2:]:
    lcmm=lcm(lcmm,i)
print(lcmm)