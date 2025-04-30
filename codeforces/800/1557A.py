t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    max_val = max(l)
    avg_rest = sum(l) - max_val
    result = max_val + avg_rest / (n - 1)
    print(f"{result:.9f}")