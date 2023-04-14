file = open("26t.txt")
k = int(file.readline())
n = int(file.readline())
a = []
for s in file:
    a.append(tuple(map(int, s.split())))
a.sort()

z = [] * k
for x, y in a:
    if k[]
print(*a, sep="\n")
