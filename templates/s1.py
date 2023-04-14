a = [int(x) for x in open("17.txt")]
ans = []
for i in range(len(a) - 2):
    if a[i] % 12 == 0 or a[i + 1] % 12 == 0 or a[i + 2] % 12 == 0:
        if a[i] % 3 == 0 and a[i + 1] % 3 == 0 and a[i + 2] % 3 == 0:
            ans.append(a[i] + a[i + 1] + a[i + 2] // 3)
print(len(ans), min(ans))
