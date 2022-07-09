n=input()
z,o=0,0
for i in n:
    if i in "zZ":
        z+=1
    else:
        o+=1
if 2*z==o:
    if "zoo" in n:
        print("Yes")
    else:
        print("No")
else:
    print("No")