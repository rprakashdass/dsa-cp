str1, str2 = input(), input()
for i in range(len(str1)):
    if str1[i].upper() > str2[i].upper():
        print(1)
        break
    elif str1[i].upper() < str2[i].upper():
        print(-1)
        break
else:
    print(0)