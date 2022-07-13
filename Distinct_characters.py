s1=input().lower()
c=""
for i in s1:
    if i not in c and i!=" ":
        c+=i
print("".join(sorted(list(c))))