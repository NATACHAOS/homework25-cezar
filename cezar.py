# """ Шифр Цезаря """
alpha = ' abcdefghijklmnopqrstuvwxyz'
n = 4
s = input().strip()
res = ''
for c in s:
    res += alpha[(alpha.index(c) + n) % len(alpha)]
print('Result: "' + res + '"')