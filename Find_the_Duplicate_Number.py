n=int(input())
l=list(map(int,input().split()))
for i in l:
    if l.count(i)==2:
        print(i)
        break
