ans = ""
string = input()
for s in string:
    if s not in "aeiouyAEIOUY":
        ans += f".{s.lower()}"

print(ans)