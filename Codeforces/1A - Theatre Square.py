import math
n, m, a = tuple(map(int, input().split()))
side1 = math.ceil(n / a)
side2 = math.ceil(m / a)
result = side1 * side2
print(result)