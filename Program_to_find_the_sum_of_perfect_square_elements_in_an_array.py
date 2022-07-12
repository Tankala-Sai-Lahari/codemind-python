n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    if int(i**0.5)==i**0.5:
        s+=i
print(s)