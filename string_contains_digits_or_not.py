n=int(input())
for z in range(n):
    n=input().split("@")
    if n[0].isalpha():
        print("No")
    else:
        print("Yes")