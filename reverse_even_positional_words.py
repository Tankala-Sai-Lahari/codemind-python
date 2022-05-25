l=input().split()
for i in range(0,len(l),2):
    l[i]=l[i][::-1]
print(*l)