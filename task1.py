def mx(a):
    r = 0
    for i in a:
        if i > r:
            r = i
    return r

s = input().split()
a = []
for i in s:
    a.append(int(i))
print(mx(a))