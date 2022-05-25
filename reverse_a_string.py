s=input().split()
t=[]
for i in s:
    a=""
    for j in i[::-1]:
        a=a+j
    t.append(a)
print(*(t[::-1]))