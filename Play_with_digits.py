n=int(input())
l=list(map(int,input().split()))
sum=0
for i in l:
    for j in str(i):
        sum+=int(j)
print(sum)