num=int(input())
l=[0,1]
print(*l,end=" ")
for i in range(num-2):
    print(l[-1]+l[-2],end=" ")
    l.append(l[-1]+l[-2])
