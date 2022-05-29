n=int(input())
e,o=0,0
l=list(map(int,input().split()))
for i in range(n):
   if i%2==0:
       e+=l[i]
   else:
       o+=l[i]
print(abs(e-o))