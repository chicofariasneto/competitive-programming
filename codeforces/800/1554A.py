t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x, y = -1, -1
    for i in a:
        if i > x: x = i
        elif i > y: y = i
    print(x * y)