t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    l, b = 101, 0
    r = [-1] * 102
    for i in range(len(s)):
        r[s[i]] = i + 1
        l = min(s[i], l)
        b = max(s[i], b)

    print(r[l], r[b])