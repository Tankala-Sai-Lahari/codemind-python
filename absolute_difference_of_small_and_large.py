l=input().split()
for i in l:
    print(abs(ord(min(i))-ord(max(i))),end=" ")