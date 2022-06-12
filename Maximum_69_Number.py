n=list(input())
for i in range(len(n)):
    if n[i]=='6':
        n[i]='9'
        break
print(int("".join(n)))