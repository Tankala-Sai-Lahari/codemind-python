s=input()
for i in "aeiou":
    if i not in s:
        print(False)
        break
else:
    print(True)