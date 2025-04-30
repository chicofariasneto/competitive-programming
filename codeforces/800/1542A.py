t = int(input())
for _ in range(t):
    n = int(input())
    numbers = input()
    s = list(map(int, numbers.split()))

    odd = 0
    even = 0
    for i in s:
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    print('Yes' if odd == even else 'No')
