s=input()
c=0
for i in s:
    if i in "!@#$%^&*()_+{}|[]>,.?/:;'":
        c+=1
print(c)