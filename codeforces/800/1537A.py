t = int(input())
for _ in range(t):
    numbers = list(map(int, input().split()))
    l = len(numbers)
    total = sum(numbers)
    c = total - l if total >= l else 1
    print(c)
