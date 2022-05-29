n=int(input())
l=list(map(int,input().split()))
t=[]
for i in l:
    if i%2!=0 and i not in t:
        t.append(i)
print(sum(list(set(t))))