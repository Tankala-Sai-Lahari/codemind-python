l=list(input())
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
if len(l)==len(l1):
    print("Unique Number")
else:
    print("Not Unique Number")