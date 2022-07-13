l=list(input())
s=[]
for i in l:
    if i!=" ":
        s.append(i)
print(min(s),s.count(min(s)),max(s),s.count(max(s)))