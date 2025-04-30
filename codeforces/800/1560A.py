r = []
a = 1
for i in range(1000):
    while a % 3 == 0 or f"{a}"[-1] == "3":
        a += 1
    r.append(a)
    a += 1

t = int(input())
for _ in range(t):
    n = int(input())
    print(r[n - 1])
