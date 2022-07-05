n=int(input())
l=list(map(int,input().split()))
if len(l)<=1:
    print("no")
else:
    for i in range(n-1):
        if l[i]<=l[i+1]:
            print("no")
            break
    else:
        print("yes")
        