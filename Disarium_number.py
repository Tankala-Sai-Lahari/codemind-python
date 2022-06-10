n=int(input())
num=n
c=len(str(n))
s=0
while n>0:
    s+=(n%10)**c
    c-=1
    n//=10
if num==s:
    print(True)
else:
    print(False)