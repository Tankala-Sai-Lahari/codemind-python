t=int(input())
for z in range(t):
    n=int(input())
    l=input()
    for i in l:
        if l.count(i)==1:
            print(i)
            break
    else:
        print(-1)
    