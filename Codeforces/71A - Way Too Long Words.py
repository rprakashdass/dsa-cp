t = int(input())
while t > 0:
    word = input()
    if len(word) > 10:
        print(word[0] + str(len(word)-2) + word[-1])
    else:
        print(word)
    t-=1