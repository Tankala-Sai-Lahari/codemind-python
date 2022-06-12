n=int(input())
s=n
while s>9:
    s=0
    while n>0:
        s+=n%10
        n//=10
    n=s
print(s)