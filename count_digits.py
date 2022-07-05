n=int(input())
l=list(map(int,input().split()))
for i in l:
    if i>=0:
        print(len(str(i)),end=" ")
    else:
        print(len(str(i))-1,end=" ")