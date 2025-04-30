t = int(input())
for _ in range(t):
    n = int(input())
    coin = int(n / 3)
    rest = n % 3
    if rest == 0:
        print(f"{coin} {coin}")
    elif rest == 1:
        print(f"{coin + 1} {coin}")
    elif rest == 2:
        print(f"{coin} {coin + 1}")
