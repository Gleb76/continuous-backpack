
n, W = map(int, input().split())
s = 0
lst = []
for i in range(n):
    c, w = map(float, input().split())
    lst += [[c/w, w]]
for i, j in sorted(lst, key = lambda x: (x[0]), reverse = True):
    if W > 0 and j <= W:
        s += i * j
        i -= i
        W -= j
    else:
        s += W * i
        break
print(round(s, 3))