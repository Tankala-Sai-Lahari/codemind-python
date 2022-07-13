l=input().lower().split()
s=0
for i in l:
    s+=abs(ord(max(i))-ord(min(i)))
print(s)