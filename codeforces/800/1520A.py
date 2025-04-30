t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    m = {}
    current = s[0]

    resp = 'YES'
    for i in range(1, n):
        if s[i] != current and m.get(s[i], False):
            resp = 'NO'
            break
        m[current] = True
        current = s[i]
    print(resp)