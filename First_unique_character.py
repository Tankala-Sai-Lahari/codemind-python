s=input().lower()
for i in s:
    if s.count(i)==1:
        print(i)
        break
else:
    print(-1)