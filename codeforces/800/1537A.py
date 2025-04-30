t = int(input())
for _ in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    l = len(numbers)
    total = sum(numbers)
    c = total - l if total >= l else 1
    print(c)
