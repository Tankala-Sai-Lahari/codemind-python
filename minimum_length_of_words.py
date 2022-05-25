l=input().split()
c=len(l[0])
for i in l:
    if c>len(i):
        c=len(i)
print(c)