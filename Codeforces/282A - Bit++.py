n = int(input())
x = 0
while n > 0:
    exp = input()
    if exp.count('+') > 0:
        x += 1
    else:
        x -= 1
    n-=1
print(x)