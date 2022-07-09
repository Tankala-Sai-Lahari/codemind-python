n=[2,3,9]
t=int(input())
for z in range(t):
    c=0
    l1,l2=map(int,input().split())
    for i in range(l1,l2+1):
        if i in n or i%10 in n:
            c+=1
    print(c)